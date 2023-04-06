import pandas as pd
from textblob import TextBlob

def read_reviews(file_path):
    return pd.read_csv(file_path)

def analyze_sentiment(reviews):
    sentiment_scores = []
    positive_count = 0
    neutral_count = 0
    negative_count = 0

    for review in reviews:
        sentiment = TextBlob(review).sentiment.polarity
        sentiment_scores.append(sentiment)

        if sentiment > 0:
            positive_count += 1
        elif sentiment == 0:
            neutral_count += 1
        else:
            negative_count += 1

    return sentiment_scores, positive_count, neutral_count, negative_count

def main():
    reviews_data = read_reviews('customer_reviews.csv')
    sentiment_scores, positive_count, neutral_count, negative_count = analyze_sentiment(reviews_data['Review'])

    average_sentiment_score = sum(sentiment_scores) / len(sentiment_scores)

    print("Average Sentiment Score:", average_sentiment_score)
    print("Number of Positive Reviews:", positive_count)
    print("Number of Neutral Reviews:", neutral_count)
    print("Number of Negative Reviews:", negative_count)

if __name__ == "__main__":
    main()
