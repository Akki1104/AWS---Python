dict = {
    # a characters
    "amazon" : "a large, strong, and aggressive woman","abstract" : "Existing only in the mind","annihilate" : "kill in large numbers","anomaly" : "deviation from the normal or common order, form, or rule",
    # b characters
    "ban" : "prohibhit especially by law or social pressure","barrage" : "the heavy fire of artillery to saturated an area","boast"  : "possess or display some desirable feature","boycott" : "refuse to sponsor; refuse to do bussiness with",
    # c characters
    "cartographer" : "a person who makes maps","cease" : "put an end to a state or an activity","collusion" : "screat agent","compulsory" : "required by rule",
    # d characters
    "dally" : "waste time","defame" : "charge falsely or with malicious intent","discord" : "lack of agreement or harmony","dispatch" : "the act of sending off something",
    # e characters
    "edify" : "make understand","elusive" : "skillful at evading capture","emulate" : "strive to equal or match, especially by imitaing","evolve" : "call forth, as an emotion, feeling, or response",
    # f character
    "flaunt" : "display proudly","flora" : "all the plant life in a particularr region or period","flux" : "a state of constant change","florecast" : "a prediction about how something will develop",
    # g character
    "garb" : "provide with clothes or put clothes on","garment" : "an article of clothing","generic" : "relating to our application to an entire class or group","genetic" : "of a segment of DNA involved in producing polypeptide chains",
    # h character
    "habitat" : "the type of environment in which an organism normally lives","hale" : "exhibiting or restored to vigorous good health","halt" : "cause to stop","harmony" : "compatibility in opinion and action",
    # i character
    "idle" : "silly or trivial","implicit" : "being without doubt or reverse","imply" : "express or state indirectly","inane" : "devoid of intelligence",
    #j character
    "justify" : "depend, explain, or make excuses for authority","juxtapose":"place side by side","junta":"a group of officers who rule a country after seizing power","juggernaut":"a massive inexorable force",
    #k character
    "kindle" : "cause to start burning","knoll" : "a small natural mound","ken" : "range of what once can know or understand","kinetic":"characterized of motion",
    # l character
    "lancet":"an acutely pointed Gothic arch","laudable":"worthy of high praise","legacy":"a gift of personal property by will","legislate":"make laws or bills",
    # m character 
    "magnitude":"the property of relative size or extent","malice":"the desire to see others suffers","manipulate":"influence or control shrewdly or deviously","manumit":"free from slavery or servitude",
    # n character
    "nadir":"the lowest point of anything","naive":"marked by or showing unaffected simplicity","negative":"having the quality of something harmful or unpleasant","neglect" :"fail to attend to",
    # o character
    "objective" : "the goal intended to be attained","oblivious":"lacking conscoius awareness of","obscure":"not clearly understood or expressed","obsolete":"no longer in use",
    # p character
    "paradigm":"a standard or typically example","paradox":"a statement that contradicts itself","paragon":"model of excellence or perfection of a kind","pastoral":"idyllically rustic",
    # q character
    "quack":"the sound made by a duck","quadrilateral":"a four-sided polygon","quaint":"attractively old-fashioned","quarrel":"an angry dispute", 
    # r character
    "rarefied":"or high moral or intellectual","ravenous":"extremely hungry","reap":"get or derive","recrimination":"mutual accusations",
    # s character
    "sagacious":"acutely insightful and wise","salubrious":"promoting health","sardonic":"disdainfully or ironically humorous","satiate":"fill to satisfaction",
    # t character
    "taper":"diminish gradually","tariff":"government tax on import or exports","taut":"pulled or drawn right","tawdry":"tastelessly showy",
    # u character
    "ubiquitous":"being present everywhere at once","ultimatum":"a final peremptory demand","unabashed":"not embarrassed","unanimous":"in complete agreement",
    # v character
    "vacuous":"devoid of intelligence","valor":"courage when facing danger","vanity":"the trait of being unduly conceited","vile":"morally reprehensible",
    # w character
    "wax":"increase,rise, or advance","warranty":"written assurance that a product or service will be provided","waver":"be unsure or weak","waylay":"wait in hiding to attack","weary":"physically and mentally fatigued",
    # x character
    "xenophobia":"a fear of foreigners or strangers",
    # y character
    "yahoo":"a person who is not intelligent or interested in culture.","yearn":"desire strongly or persistently","yelp":"a sharp high-pithced cry","yen":"the basic unit of money in japan",
    # z character
    "zephyr":"a slight wind","zany":"indicrous or foolish","zeal":"a feeling of strong eagerness","zenith":"the highest point of something"
} 
def find(value):
    len_value = len(value)
    dic_key = list(dict.keys())
    chk = True
    for element in dic_key:
        if element[:len_value].lower() == value.lower():
            chk = False
            print(element+" : \t"+dict.get(element)+"\n")
    if chk:
        print("Element is not found in the Dictionary\n\n")
     
        
while True:
    var = input("\n\n\nEnter the characters to search in Dictionary (Q1 for Quit) : ")
    if var.lower() == 'q1':
        print("Good Bye !")
        break
    else:
        find(var)