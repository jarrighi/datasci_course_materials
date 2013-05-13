import sys
import json

def print_top_ten_tags(tweet_file):
  tags = get_tag_counts(tweet_file)
  print_top(10, tags)

def get_tag_counts(tweet_file):
  tag_counts = {}
  total_count = 0
  for item in tweet_file :
    tweet = json.loads(item)
    if 'text' in tweet:
      tweet_text = tweet['text']
      for word in tweet_text.split():
        if word[0] == '#':
          if word in tag_counts:
            tag_counts[word] += 1
            total_count += 1
          else:
            tag_counts[word] = 1
            total_count += 1
  for tag in tag_counts:
    tag_counts[tag] = float(tag_counts[tag]) / float(total_count)
  return tag_counts

def print_top(n, tags):
  for i in sorted(tags, key=tags.get, reverse=True)[:n]:
    print i, tags[i]

def main():
  tweet_file = open(sys.argv[1])
  print_top_ten_tags(tweet_file)

if __name__ == '__main__':
  main()