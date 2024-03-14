import numpy as np

class SimpleRecommendationSystem:
    def __init__(self, num_users, num_items):
        self.num_users = num_users
        self.num_items = num_items
        self.ratings = np.zeros((num_users, num_items))

    def add_rating(self, user_id, item_id, rating):
        self.ratings[user_id][item_id] = rating

    def get_similar_users(self, user_id, num_neighbors=5):
        user_ratings = self.ratings[user_id]
        similarities = []
        for i in range(self.num_users):
            if i != user_id:
                other_user_ratings = self.ratings[i]
                similarity = np.dot(user_ratings, other_user_ratings) / (
                            np.linalg.norm(user_ratings) * np.linalg.norm(other_user_ratings))
                similarities.append((i, similarity))
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:num_neighbors]

    def recommend_items(self, user_id, num_recommendations=5):
        similar_users = self.get_similar_users(user_id)
        recommendations = {}
        for neighbor_id, similarity in similar_users:
            neighbor_ratings = self.ratings[neighbor_id]
            for i in range(self.num_items):
                if neighbor_ratings[i] != 0 and self.ratings[user_id][i] == 0:
                    if i not in recommendations:
                        recommendations[i] = neighbor_ratings[i] * similarity
                    else:
                        recommendations[i] += neighbor_ratings[i] * similarity
        recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
        return recommendations[:num_recommendations]


if __name__ == '__main__':
   
    num_users = 5
    num_items = 10
    recommendation_system = SimpleRecommendationSystem(num_users, num_items)

 
    recommendation_system.add_rating(0, 1, 4)
    recommendation_system.add_rating(0, 3, 5)
    recommendation_system.add_rating(1, 0, 3)
    recommendation_system.add_rating(1, 2, 5)
    recommendation_system.add_rating(2, 3, 4)
    recommendation_system.add_rating(2, 5, 3)
    recommendation_system.add_rating(3, 1, 2)
    recommendation_system.add_rating(3, 4, 4)
    recommendation_system.add_rating(4, 2, 5)
    recommendation_system.add_rating(4, 7, 2)


    user_id = 0
    recommendations = recommendation_system.recommend_items(user_id)
    print("Recommendations for user", user_id)
    for item_id, score in recommendations:
        print("Item:", item_id, "Score:", score)
