# COMMKnows 📰

**- Inspiration 💡** <br>
Have you gotten tired of reading tons of news through the website every day and feel exhausted to focus? Living in a
fast-paced lifestyle, we always want to have a  **more efficient way to read the news** and explore what is happening
around the world. Thus, our team wants to develop a responsive website that provides a smarter way for you to read news
on your commuting bus to school or work, in the 10min break between your classes, or when you wait in the line for
today's bubble tea!

**- What is does ❓** <br>
This website will provide you with a brand new to efficiently read the news! It will select 6 worldwide commerce-related
news each day. You are able to see the title, a descriptive image, and a brief introduction for each one. If you are
getting interested in a particular piece of news, clicking the URL provided at the end of each news will direct you to
the original news source.

**- How we built it 💻** <br>
We start our work by creating the template for our  website using HTML. Our template includes the title, descriptive image, brief introduction, and a URL to the original news source. Then, we build our backend by using Python and Flask, fetching the raw data from the API and parsing it into the human-readable format. Furthermore, it also fills in the template we build at the begging using Ginger, providing all the functions we required for this project. Moving to the deployment part, we use nginx as the server, allowing users to send HTTP requests to the web app and communiting with it.

**- Challenges we ran into 🧐** <br>
The biggest challenge we meet is deploying our website onto the server. We tried to use GoDaddy at first, but it does not provide root permission. Thus, we are unable to download the dependencies. Then we tried the Aliyun server which is based in China, and we have previous experience using it. However, after 3 hours of adjustment, this server was still not working since the news API we used is considered a "foreign website" and got banned in mainland China. Finally, we found the Alibabacloud server, which worked perfectly for our project and have the required root permission. After installing the git and pythone3 onto this server, we successfully deployed our website. This whole process took us over 9 hours of work. Every time we changed to another server, we needed to work from scratch to build the environment. Thankfully, everything worked out in the end, and we are happy that all these hard-workings will provide valuable experience to support our further work dealing with the server. 

**- Accomplishments that we're proud of 🥳** <br>
The most satisfactory part for us is that we learned a new language and built something truly helpful for our everyday
life! As we agree, the best way to learn a new language is by applying it. This hackathon provided us with a great
opportunity to finally start our learning in Python, and we are hoping to continue our learning after this weekend!
Besides, since our project is highly related to the university students like our teammates, we already introduced our
work to several classmates and got positive feedback! We are excited to learn more about the valuable feedback to
improve our work further.

**- What we learned 📝** <br>
We learned how to code in Python! This is the most valuable learning outcome for our teammates. Moreover, one of our
group members did not have previous experience in using API. As we help each out, she now has a basic understanding of
how API works and how to apply it in our project! Furthermore, this is the first time our group join a hackathon event,
and this project is completely built from scratch. We are happy that we developed more time management and group work
skills through this intense weekend!

**- What's next for COMMKnows 📌** <br>
Due to the time constraint of the hackathon, our group hasn't got the chance to implement the searching function. We do
believe that a searching function will help our users to explore more interesting news beyond our every day 6 pieces,
and we are hoping to further develop this function after this weekend!



