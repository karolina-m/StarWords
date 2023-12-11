This folder contains data and scripts for the paper *"Bilingual children reach early language milestones at the same age as monolingual peers: evidence from parental report via mobile app"*

The data stored here is part of data gathered in StarWords study (2019-2024, financed by National Science Centre: 2018/31/B/HS6/03916), see https://www.starwords.eu/. 
The present dataset contains anonymized information on the particular study participans whose data was analysed in the paper specified above. It is not a full dataset collected in the StarWords study.

The data presented here include:
- **words.csv** - words and neologisms of analyzed participants: their form, meaning, parental comment (if applicable), language(s) the word was assigned to, child's age in months at the moment when the word was reported, child's group (Bilingual/Monolingual) and match (1 or 2).
  - a word can be assigned to multiple languages (see columns *l1*, *l2*, *l3*)
  - *word_number* is the ordinal number of a particular word in a given language of a particular child.
- **multiwords.csv** - utterances of analyzed participants: their form, meaning, parental comment (if applicable), language(s) the multiword was assigned to, child's age when the multiword was reported, child's group, and match.
  - *words_per_utterance* is the length of the utterance in words, based on what the participant reported,
  - *m_cat* is the category of the multiword utterance: *m1* is the child's first utterance (irregardless of length), *m3* is a three-word utterance, *m4* is a four-word utterance,
  - *elements_number* is the ordinal number of a particular word in a given language of a particular child.
- **milestones.csv** - age of reaching particular milestones (i.e., babbling, walking unasssisted, babbling), as reported or recalled by parents (for more information on the reported/recalled distinction, see the paper).
- **input.csv** - basic information on the category of language input at home: Polish, Mixed (with the majority language) or NoInfo (for missing data).
- **kids.csv** - basic information on the children, used to match the bilingual and monolingual groups: children's match, group, sex, age at study entry (in months), country of living, number of languages the child has contact with, parental education level and the length of paretanl reporting. ***Children's ids are anonymized***. For more information, see the paper.
