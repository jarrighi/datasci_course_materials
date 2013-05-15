import sys
import json

STATES = {"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
      "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
      "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
      "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
      "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"}

def make_sent_dict(fn):
  lines = [l.strip().split('\t', 2) for l in fn.readlines()]
  sent_dict = {i[0]: int(i[1]) for i in lines}
  return sent_dict

def get_state(place):
  state = None
  for item in STATES:
    if item in place['full_name']:
      state = item
  return state

def calc_sent(tweet, sents):
  words = tweet.split()
  sent = 0
  for item in words:
    if item in sents:
      sent = sent + sents[item]
  return sent


def get_happiest_state(tweets, sents):
  sents_by_state = {}
  for line in tweets:
    tweet = json.loads(line)
    place = tweet.get('place', False)
    text = tweet.get('text', False)
    state = None
    if place and text:
      state = get_state(place)
    if state != None:
      sent = calc_sent(text, sents)
      if state in sents_by_state:
        sents_by_state[state] = [sents_by_state[state][0] + sent, sents_by_state[state][1]  + 1]
      else:
        sents_by_state[state] = [sent, 1.0]
  sent_dict = {}
  for i in sents_by_state:
    sent_dict[i] = sents_by_state[i][0] / sents_by_state[i][1]
  happiest_state = sorted(sent_dict, key = sent_dict.get, reverse=True)[0]
  return happiest_state


def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])
  sent_dict = make_sent_dict(sent_file)
  print get_happiest_state(tweet_file, sent_dict)

if __name__ == '__main__':
  main()