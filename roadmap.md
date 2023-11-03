# Roadmap 

The basic idea is an incremental parser that takes in an utterance, one word at a time, to:

1. Sentence completer: predict the rest of the utterance, given the context 
2. FrameNet parser: Generates a frame (represented with a graph-like schema) for sentence or partial sentence. 
3. Manager: that manages the parsing process, asking the question of whether existing parses are enough, or another needs to be run

Tasks
1. Train the FrameNet parser
  - [ ] Preprocess  to map sentence parses to corresponding TREXes. (forget trigger)
    - download dataset, explore it, and then write a script to preprocess 
    - Might be able to use [this github repo](https://github.com/chanind/frame-semantic-transformer) to help 
  - [ ] prepare the dataset for finetuning. 




