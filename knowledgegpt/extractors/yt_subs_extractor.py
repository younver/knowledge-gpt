from ..utils.utils_subtitles import scrape_youtube
from ..utils.utils_embedding import compute_doc_embeddings, compute_doc_embeddings_hf
from ..utils.utils_completion import answer_query_with_context


class YTSubsExtractor:
    def __init__(self, mongo_client, model_lang="en", embedding_extractor="hf"):
        self.mongo_client = mongo_client
        self.model_lang = model_lang
        self.embedding_extractor = embedding_extractor
        self.df = None
        self.embeddings = None

    def extract(self, video_id: str, query: str, max_tokens, to_save: bool=None):
        """
        Method that takes a YouTube video ID as input and returns the captions
        as a pandas DataFrame with the key "caption".
        :param video_id: YouTube video ID
        :param query: Query to answer
        :param max_tokens: Maximum number of tokens to use for the prompt
        :param to_save: Whether to save the embeddings to MongoDB
        :return: Tuple of the answer, prompt, and messages
        """
        print("Extracting text...")
        if not video_id:
            raise ValueError("Video ID is missing")
        if self.df is None:
            self.df = scrape_youtube(video_id)

        if self.embeddings is None:
            print("Computing embeddings...")

            if self.embedding_extractor == "hf":
                self.embeddings = compute_doc_embeddings_hf(self.df, self.model_lang)
            else:
                self.embeddings = compute_doc_embeddings(self.df)

            print("Answering query...")

        answer = ""
        if self.embedding_extractor == "hf":
            answer, prompt, messages = answer_query_with_context(query, self.df, self.embeddings, embedding_type="hf", model_lang=self.model_lang, max_tokens=max_tokens)
        else:
            answer, prompt, messages = answer_query_with_context(query, self.df, self.embeddings, embedding_type="openai", model_lang=self.model_lang, max_tokens=max_tokens)

        if to_save:
            self.mongo_client.pair_yt.insert_one({"query": query, "answer": answer, "prompt": prompt})

        print("Done!")

        return answer, prompt, messages
