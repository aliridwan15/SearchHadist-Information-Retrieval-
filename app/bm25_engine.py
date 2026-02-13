# app/bm25_engine.py
import pandas as pd
from rank_bm25 import BM25Okapi
import re 

class BM25Engine:
    def __init__(self, csv_path):
        try:
            self.df = pd.read_csv(csv_path)
            self.df['Arab'] = self.df['Arab'].fillna('')
            self.df['Terjemahan'] = self.df['Terjemahan'].fillna('')
            self.df['Perawi'] = self.df['Perawi'].fillna('')
            self.df['Perawi_Cleaned'] = self.df['Perawi'].astype(str).apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', x).strip())

            self.corpus_arab = [str(x).lower().split() for x in self.df['Arab']]
            self.corpus_terjemahan = [str(x).lower().split() for x in self.df['Terjemahan']]
            
            self.bm25_arab = BM25Okapi(self.corpus_arab)
            self.bm25_terjemahan = BM25Okapi(self.corpus_terjemahan)

            self.unique_perawi_names = sorted(self.df['Perawi_Cleaned'].dropna().unique().tolist())
            print("BM25 Engine initialized successfully.")
        except Exception as e:
            print(f"Error initializing engine: {e}")
            raise 

    def search_general(self, query, limit=None):
        tokenized_query = str(query).lower().split()
        if not tokenized_query: return []

        scores_arab = self.bm25_arab.get_scores(tokenized_query)
        scores_terjemahan = self.bm25_terjemahan.get_scores(tokenized_query)
        overall_scores = [s_a + s_t for s_a, s_t in zip(scores_arab, scores_terjemahan)]

        results_with_scores = [(overall_scores[i], i) for i in range(len(overall_scores)) if overall_scores[i] > 0]
        results_with_scores.sort(key=lambda x: x[0], reverse=True)
        
        return self._format_results(results_with_scores, limit)

    def get_hadiths_by_perawi_exact(self, perawi_name, limit=None): 
        if not perawi_name: return []
        filtered_df = self.df[self.df['Perawi_Cleaned'] == perawi_name]
        
        results = []
        for index, row in filtered_df.iterrows():
            results.append({
                'Perawi': row['Perawi'],
                'Arab': row['Arab'],
                'Terjemahan': row['Terjemahan'],
                'score': None 
            })
        
        if limit and limit != 'all':
            return results[:int(limit)]
        return results

    def search_within_perawi(self, query, perawi_name, limit=None):
        if not query or not perawi_name: return []
        
        filtered_df = self.df[self.df['Perawi_Cleaned'] == perawi_name]
        if filtered_df.empty: return []

        # Temp corpus
        temp_arab = [str(x).lower().split() for x in filtered_df['Arab']]
        temp_terjemahan = [str(x).lower().split() for x in filtered_df['Terjemahan']]
        
        if not temp_arab: return []

        temp_bm25_a = BM25Okapi(temp_arab)
        temp_bm25_t = BM25Okapi(temp_terjemahan)
        
        q_tok = str(query).lower().split()
        scores = [sa + st for sa, st in zip(temp_bm25_a.get_scores(q_tok), temp_bm25_t.get_scores(q_tok))]
        
        orig_indices = filtered_df.index.tolist()
        results_with_scores = [(scores[i], orig_indices[i]) for i in range(len(scores)) if scores[i] > 0]
        results_with_scores.sort(key=lambda x: x[0], reverse=True)

        return self._format_results(results_with_scores, limit)

    def _format_results(self, results_with_scores, limit):
        if limit and limit != 'all':
            results_with_scores = results_with_scores[:int(limit)]
            
        final = []
        for score, idx in results_with_scores:
            final.append({
                'Perawi': self.df.loc[idx, 'Perawi'],
                'Arab': self.df.loc[idx, 'Arab'],
                'Terjemahan': self.df.loc[idx, 'Terjemahan'],
                'score': round(score, 2)
            })
        return final