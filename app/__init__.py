# app/__init__.py
from flask import Flask, render_template, request
import os
from .bm25_engine import BM25Engine
import math

app = Flask(__name__)

script_dir = os.path.dirname(__file__)
csv_path_absolute = os.path.join(script_dir, 'Sunnah.csv')

try:
    engine = BM25Engine(csv_path=csv_path_absolute)
except Exception as e:
    print(f"Failed to initialize BM25 Engine: {e}")
    exit()

DEFAULT_PAGINATION_LIMIT = 15

@app.route('/')
def index():
    return render_template('index.html',
                           results=None,
                           query=None,
                           search_type='general',
                           unique_perawi=engine.unique_perawi_names,
                           selected_perawi=None,
                           search_type_display='Umum',
                           limit=str(DEFAULT_PAGINATION_LIMIT),
                           current_page=1,
                           total_pages=0)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip()
    search_type = request.args.get('search_type', 'general')
    perawi_name = request.args.get('perawi_name', '').strip()
    limit_str = request.args.get('limit', str(DEFAULT_PAGINATION_LIMIT))
    page = request.args.get('page', 1, type=int)

    results_all = []
    selected_perawi = None 
    search_type_display = 'Umum'

    if search_type == 'perawi_only':
        search_type_display = 'Perawi Spesifik'
        if perawi_name:
            results_all = engine.get_hadiths_by_perawi_exact(perawi_name, limit='all')
            selected_perawi = perawi_name
    elif search_type == 'combined':
        search_type_display = 'Kombinasi (Teks & Perawi)'
        if query and perawi_name:
            results_all = engine.search_within_perawi(query, perawi_name, limit='all')
            selected_perawi = perawi_name
    else: # general
        search_type_display = 'Umum'
        if query:
            results_all = engine.search_general(query, limit='all')

    if (search_type == 'general' and not query) or \
       (search_type == 'perawi_only' and not perawi_name) or \
       (search_type == 'combined' and (not query or not perawi_name)):
        results_all = []

    total_results = len(results_all)

    # Logika Paginasi
    if limit_str == 'all':
        current_limit_for_pagination = DEFAULT_PAGINATION_LIMIT
    else:
        try:
            current_limit_for_pagination = int(limit_str)
        except ValueError:
            current_limit_for_pagination = DEFAULT_PAGINATION_LIMIT

    if current_limit_for_pagination <= 0:
        current_limit_for_pagination = DEFAULT_PAGINATION_LIMIT

    total_pages = math.ceil(total_results / current_limit_for_pagination) if current_limit_for_pagination > 0 else 0

    # Boundary check page
    if page < 1: page = 1
    elif page > total_pages and total_pages > 0: page = total_pages
    elif total_pages == 0: page = 1

    start_index = (page - 1) * current_limit_for_pagination
    end_index = start_index + current_limit_for_pagination
    results_paginated = results_all[start_index:end_index]

    return render_template('index.html',
                           results=results_paginated,
                           query=query,
                           search_type=search_type,
                           unique_perawi=engine.unique_perawi_names,
                           selected_perawi=selected_perawi, # Pass selected perawi agar dropdown tetap terpilih
                           search_type_display=search_type_display,
                           limit=limit_str,
                           current_page=page,
                           total_pages=total_pages,
                           total_results=total_results)

@app.route('/about')
def about():
    # Kamu perlu buat about.html terpisah jika ingin halaman ini bekerja
    return render_template('about.html', unique_perawi=engine.unique_perawi_names)

if __name__ == '__main__':
    app.run(debug=True)