from collections import namedtuple
from google.cloud import language_v1

data_set = []  
cleaned_set = set()
name_set = set()

def sample_analyze_entities(text_content):
    """
    Analyzing Entities in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})

    # Loop through entitites returned from the API
    # print(response.entities)
    for entity in response.entities:
        data_set.append((u"{}".format(entity.name), u"{}".format(entity.salience)))
        cleaned_set.add((u"{}".format(entity.name), 0))
        name_set.add(u"{}".format(entity.name))
        # Get the salience score associated with the entity in the [0, 1.0] range

        # print(u"{}".format(entity.name), u"{}".format(entity.salience))

        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        # print(u"Entity type: {}".format(language_v1.Entity.Type(entity.type_).name))



        # Loop over the metadata associated with entity. For many known entities,
        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.
        # for metadata_name, metadata_value in entity.metadata.items():
        #     print(u"{}: {}".format(metadata_name, metadata_value))

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.
        # for mention in entity.mentions:
        #     print(u"Mention text: {}".format(mention.text.content))

            # print(
            #     u"Mention type: {}".format(language_v1.EntityMention.Type(mention.type_).name)
            # )

    # print(u"Language of the text: {}".format(response.language))


message = 'On Aug. 15, Prime Minister Justin Trudeau visited newly minted Governor General Mary Simon in order to dissolve Parliament and call a snap election. He argued that this election would allow Canadians to have a say in who should guide Canadians out of the pandemic.Of course, the prime minister’s greater goal was to seize the (perceived) opportunity to win a majority government. Neither the arrival of the election, nor the prime minister’s motives, were a surprise to Canadians. But Trudeau himself appears surprised to learn that Canadians did not want an election, which is clearly having a detrimental impact on Liberal fortunes in the polls.Historically, Conservative leaders typically own the unenviable label of being the leader that Canadians believe has a hidden agenda. However, Canadians say it is the Liberal leader who has the ulterior motive this time around.Read more: Pandemic elections — How have other countries voted during COVID-19? The Liberals were in a strong position heading into the election. Approval ratings of Trudeau’s performance have been strong, on the heels of a successful rollout of the COVID-19 vaccine in Canada. Moreover, Ipsos polling throughout 2021 has placed the Liberals in the driver’s seat, at one point enjoying a double-digit lead over the second-place Conservatives in the national popular vote. Earlier in summer, the gap between the leading parties shrunk to six points. If the Liberals could win a plurality of seats and form a minority government despite having lost the popular vote to the Tories in 2019, then even a six-point lead over the Conservatives should give them a good shot at forming a majority government, right? Wrong. The miscalculation of the Liberal Party in believing that Canadians would be okay with an election campaign amidst the fourth wave of the pandemic might be their undoing, or at the very least, prevent them from winning a majority mandate. At the start of the campaign, 56 per cent of Canadians said that we should not be having an election during a pandemic. In the absence of a compelling argument from Trudeau articulating why an election is necessary, the proportion of Canadians who feel we shouldn’t be in a campaign right now has grown to 69 per cent. Moreover, one in four Canadians say they do not feel safe voting in person. Exacerbating the challenges of the Liberal government is the absence of a dominant wedge issue. Canadians say that the pandemic, affordability, the economy, health care, housing and climate change are among the most important issues to them. Liberal Leader Trudeau has tried to create a wedge issue out of a number of these, including health care, climate change, gun control and abortion rights, but Conservative Party Leader Erin O’Toole has largely avoided the wedge by saying that he supports the health-care system Canada currently has, that he believes in climate change, and that he is pro-choice. The gun control wedge is working somewhat within Quebec, preventing the Conservatives from gaining too much traction in la belle province. Therefore, we’re left with an election campaign with no clear top issue to drive the narrative. Without a key wedge between himself and O’Toole, Trudeau is once again answering what has become a familiar question in this campaign: why are we having an election? Through their shifting vote intentions compared to the start of the campaign, Canadians are indicating that a compelling answer remains elusive. Read more: Here’s what’s different about this year’s federal election in Canada. The election has given Canadians an opportunity to get a closer look at the other party leaders. Over the last 18 months, the prime minister has dominated the news — and rightly so — as Canadians have rallied around their leaders during these challenging circumstances. This left O’Toole, NDP Leader Jagmeet Singh and the other leaders struggling for airtime. The campaign has put a spotlight on the opposition leaders, and Canadians like what they’re seeing. Singh is seen as the most likeable of all the party leaders, while perceptions of O’Toole are also improving, as many Canadians believe that he isn’t the boogeyman that Trudeau is trying to portray him as. The solid lead the Liberals once enjoyed has evaporated, and we have a horserace on our hands. There is a good chance that we will end up back where we started, with a Liberal minority government. This is likely the best-case scenario for the Liberals. And if they do win with a Parliament that looks a lot like the previous one, Trudeau may once again need to explain to Canadians why we had an election. Not an enviable position for the start of one’s next mandate.'
sample_analyze_entities(message)
# print(data_set)
# print(name_set)


# def average_salience(names):
#     for x in names:
#         denom = data_set[0].count(x)
#         salience = data_set[1].sum

    

#print(cleaned_set)
#steralized_data=[]

