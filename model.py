from sentence_transformers import SentenceTransformer, util
import json

model = SentenceTransformer('all-MiniLM-L6-v2')

with open('data.json', 'r') as f:
    data = json.load(f)

questions = [item['question'] for item in data]
answers = [item['answer'] for item in data]

question_embeddings = model.encode(questions, convert_to_tensor=True)

def get_response(user_input):
    user_embedding = model.encode(user_input, convert_to_tensor=True)
    scores = util.cos_sim(user_embedding, question_embeddings)
    best_match = scores.argmax()
    return answers[best_match]