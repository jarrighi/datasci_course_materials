import sys
import json

def print_word_frequencies(tweet_file):
  word_counts = {}
  total_count = 0
  for item in tweet_file :
    tweet = json.loads(item)
    if 'text' in tweet:
      tweet_text = tweet['text']
      for word in tweet_text.split():
        if word in word_counts:
          word_counts[word] += 1
          total_count += 1
        else:
          word_counts[word] = 1
          total_count += 1
  for word in word_counts:
    print word,
    print float(word_counts[word] / total_count)

    

def main():
  tweet_file = open(sys.argv[1])
  print_word_frequencies(tweet_file)

if __name__ == '__main__':
  main()