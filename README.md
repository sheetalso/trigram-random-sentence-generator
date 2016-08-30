# Random Sentence Generation From Trigrams

</br>
Takes a text file as input and returns (semi-) coherent sentences, albeit with most of the meaning lost.
Results get better as the size of your text input gets larger. 

</br>
Sample result drawn from a corpus of political commentary:

<ul>
  <em>"Also apparently trump called in to news shows DURING the convention yesterday. they are old, etc. anything? same. Right. He should get it for 50 years for goodness sakes. It's frustrating. I would prob vote for fast track for Obama on TPP? And sure enough, it was recent history. Same deal as batman v superman. I love him. I am on ep 4."</em>
</ul>

</br>
Occasionally it will return actual phrases/sentences from the text input, particularly with a smaller corpus. This is because we begin each sentence with a "start" word and choose randomly from all the possible words that can follow that word -- if there's only one possible word that follows the "start" word, you can see how the original sentences might be reproduced. 
