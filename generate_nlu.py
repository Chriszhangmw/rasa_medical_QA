
'''

## intent:chitchat
- what is rasa
- what is rasa [core](product)
- what is rasa [core](product)?
- what is rasa actually
- what is rasa?

'''



ask_words = ["find the","show the","what is the"]
subject_entity = ["pmserver","vmserver","server"]
relation_words = ["host by"]
object_entity = ["datacenter","business","pmserver"]
attribute_searchable = {
    "datacenter":["hk1","hk2","hk3","hk4","hk5","hk6"],
    "business":["mysql","wiseeye","jjbak","lki","fuo"],
    "pmserver":["1.1.1.1","2.2.2.2","3.3.3.3","4.4.4.4","5.5.5.5","3.21.2.4","5.6.7.8","8.7.9.0"],
    "vmserver":["1.1.1.1","2.2.2.2","3.3.3.3","4.4.4.4","5.5.5.5","3.21.2.4","5.6.7.8","8.7.9.0"],
    "server":["1.1.1.1","2.2.2.2","3.3.3.3","4.4.4.4","5.5.5.5","3.21.2.4","5.6.7.8","8.7.9.0"]
}
attribute = ["cpu","memory","disk","hostname","city","name","io","region"]
all_entity = ["datacenter","business","pmserver","vmserver","server"]

#attribute
def get_attribute(intent_name,num_samples):
    intent_name = str(intent_name)
    nlu = open('nlu2.md','w')
    nlu.write('##intent: ' + intent_name + '\n')
    samples = set()
    for ask_w in ask_words:
        for a in attribute:
            for t in all_entity:
                for attribute_value in attribute_searchable[t]:
                    line1 = '- ' + ask_w + ' ' + '[' + a + ']' +'(' + "attribute" + ')' + ' of ' + '[' + t + ']' + '(' + "entity_type" + ')' + '\n'
                    line2 = '- ' + ask_w + ' ' + '[' + a + ']' + '(' + "attribute" + ')' + '\n'
                    line3 = '- ' + ask_w + ' ' + '[' + a + ']' + '(' + "attribute" + ')' + ' of ' + '[' + t + ']' + '(' + "entity_type" + ')' +  ' ' + '[' + attribute_value + ']' + '(' + "attribute_searchable" + ')'+'\n'
                    line4 = '- ' + ask_w + ' ' + '[' + attribute_value + ']' + '(' + "attribute_searchable" + ')' + '\n'
                    samples.add(line1)
                    samples.add(line2)
                    samples.add(line3)
                    samples.add(line4)
                    nlu.write(line1)
                    nlu.write(line2)
                    nlu.write(line3)
                    nlu.write(line4)
                    if len(samples) > num_samples:
                        break


#relation
def get_relation(intent_name,num_samples):
    intent_name = str(intent_name)
    nlu = open('nlu1.md','w')
    nlu.write('##intent: ' + intent_name + '\n')
    samples = set()
    for ask_w in ask_words:
        for s in subject_entity:
            for relation in relation_words:
                for o in object_entity:
                    for attribute_value in attribute_searchable[o]:
                        line1 = '- ' + ask_w + ' ' + '[' + s + ']' +'(' + "subject_entity" + ')' + ' ' + relation + ' ' + '[' + o + ']' + '(' + "object_entity" + ')' + ' ' + '[' + attribute_value + ']'+'(' + "attribute_searchable" + ')' + '\n'
                        line2 = '- ' + ask_w + ' ' + '[' + s + ']' + '(' + "subject_entity" + ')' + ' ' + relation +  ' ' + '[' + attribute_value + ']' + '(' + "attribute_searchable" + ')' + '\n'
                        line3 = '- ' + ask_w + ' ' + '[' + s + ']' + '(' + "subject_entity" + ')' + ' ' + relation + '\n'
                        samples.add(line1)
                        samples.add(line2)
                        samples.add(line3)
                        nlu.write(line1)
                        nlu.write(line2)
                        nlu.write(line3)
                        if len(samples) > num_samples:
                            break
    nlu.close()





if __name__ == "__main__":
    get_relation("query_host", 500000)
    get_attribute("query_attribute",500000)