import sys
import json

def print_top_ten_tags(tweet_file):
  tags = get_tag_counts(tweet_file)
  print_top(10, tags)

def get_tag_counts(tweet_file):
  tag_counts = {}
  for item in tweet_file:
    tweet = json.loads(item)
    if 'entities' in tweet:
      tags = tweet['entities']['hashtags']
      for tag in tags:
        word = tag['text']
        if word in tag_counts:
          tag_counts[word] += 1
        else:
          tag_counts[word] = 1.0
  return tag_counts

def print_top(n, tags):
  for i in sorted(tags, key=tags.get, reverse=True)[:n]:
    print i, tags[i]

def main():
  tweet_file = open(sys.argv[1])
  print_top_ten_tags(tweet_file)

if __name__ == '__main__':
  main()