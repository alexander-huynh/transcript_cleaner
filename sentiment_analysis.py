import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Ensure you have the VADER lexicon
nltk.download('vader_lexicon')

def preprocess_text(text):
    # Lowercasing and removing special characters
    text = text.lower()
    # Add any other preprocessing steps as needed
    return text

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    return sentiment_scores

def plot_sentiment_distribution(sentiment_scores):
    labels = ['Negative', 'Neutral', 'Positive']
    scores = [sentiment_scores['neg'], sentiment_scores['neu'], sentiment_scores['pos']]

    plt.bar(labels, scores, color=['red', 'gray', 'green'])
    plt.xlabel('Sentiment')
    plt.ylabel('Score')
    plt.title('Sentiment Distribution')
    plt.show()

def main():
    # Sample transcript text
    transcript_text = """
    we're no strangers to love you know the rules and so do I I full commitments while I'm thinking of you wouldn't get this from any other guy I just want to tell you how I'm feeling got to make you understand Never Going To Give You Up never going to let you down never going to run around and desert you never going to make you cry never going to say goodbye never going to tell a lie and hurt you we've known each other for so long your heart's been aching but your to sh to say it inside we both know what's been going on we know the game and we're going to playing and if you ask me how I'm feeling don't tell me you're too my you see Never Going To Give You Up never going to let you down never to run around and desert you never going to make you cry never going to say goodbye never going to tell a lie and hurt you never going to give you up never going to let you down never going to run around and desert you never going to make you cry never going to sing goodbye going to tell a lie and hurt you give you give you going to give going to give you going to give going to give you we've known each other for so long your heart's been aching but you're too sh to say inside we both know what's been going on we the game and we're going to play it I just want to tell you how I'm feeling got to make you understand Never Going To Give You Up never going to let you down never going to run around and desert you never going to make you cry never going to say goodbye never going to tell you my and Hurt You Never Going To Give You Up never going to let you down never going to run around and desert you never going to make you C never going to say goodbye never going to tell and Hur You Never Going To Give You Up never going to let you down never going to run around and desert you never going to make you going to goodbye and
    """

    # Preprocess and analyze sentiment
    preprocessed_text = preprocess_text(transcript_text)
    sentiment_scores = analyze_sentiment(preprocessed_text)
    
    print(f"Sentiment Scores: {sentiment_scores}")
    
    # Plot sentiment distribution
    plot_sentiment_distribution(sentiment_scores)

if __name__ == "__main__":
    main()
