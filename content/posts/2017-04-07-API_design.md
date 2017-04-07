Title: How to completely fail at API design
Date: 2017-04-07
header_cover: /images/code_head.jpg
Category: general
Tags: API

API design is a difficult topic.  A lot of people have opinions about it and
also nearly all of those people who have opinions are the **wrong** people to
ask about it.  Since you are reading an article about APIs it is fairly safe to
assume that you already have at least some opinions about it already.  You are
perhaps here to read my screed against GraphQL or REST or similar topic, but I
am going to disappoint you there.

In fact, if you're trying to figure out if you should build a GraphQL or REST
API and you haven't answered one, simple question first then you are already
well on the way to failing to build the correct API.  You have put the cart
before the horse and also when you realize the cart should be a plane, your
horse will *die*.  If you don't want to be a horse murderer, put aside the fact
that I just said you are failing and please consider this question for a moment.  

## THE Question

The first question of API design you should answer is this:

> Should the API support building a feature complete, better looking version of
> the user interface?

Think about this for just a moment.  If you are a developer of APIs you've
perhaps heard of companies adding restrictive permissions or throttling to
their APIs that make building a client impossible after someone build a much
better app or site already.  If you are not a developer then you may have heard
ominous stories about company X "locking out third-party developers" or
"shutting down ABC other service" or "accidentally murdering a horse in public"
(metaphorically, of course).  Regardless of which of those two camps you're in,
hopefully we can all agree that you don't want to be responsible for making
that happen to your company.

The failure here is changing the answer to that question at some point from Yes
to No.  If you answer "Yes" that you want to allow other people to do a better
job of building your own application than you have done, that is fine.  If you
answer "No" that you want your users to stay on your site for their main
experience, that is fine too.  But if you answer "Yes" today and "No" after
you're successful tomorrow, then you are in for a wild ride.  It might even be
so bad that business people or, you know, shareholders/VCs find out.  So there can
be a real cost to answering the question incorrectly.

## Ignorance is no excuse

For the business people out there, I have something to tell you.  If you went
to a developer and told them to "Make an API for our product" without any clear
instructions or limitations then they have answered this question for you and
their answer, almost certainly, was "Yes."  

As I said, Yes can be a perfectly valid answer to this question but only if you
are prepared for what it means.  Imagine in your head for a moment that your
wildest fantasy has come true (about your product... keep it clean, people).
Your product is beautiful and stylish and easy to use.  You see a user in front
of it Getting Things Done&trade;.  They don't accidentally click the delete
button when they want to save, they aren't missing the widget they want to
click even though it is *right there*, and the whole thing is pretty and fast.
Now imagine that the interface that person is using isn't made by your company.
Sure, it is using your services underneath, but some random person on the
internet you've never even heard of made that interface and it is ***better*** than
the one you agonize over every day with your development team.  

Are you happy?  Will your boss be happy?

Again, "Yes" is a perfectly valid and perfectly lovely answer.   If that's your
answer, wonderful.  You've got a product that does its job, an API that enables
developers to work with your company, and people that are interested in putting
in their own time to do just that.  Take a long lunch and enjoy your day.

But a lot of business people would be absolutely terrified and upset by this
situation.  If the first reaction you had to that situation was "There's got to
be some way to shut this down!" then your answer is "No" and you need to know
that.  Your developers need to know that.  If your business is based on selling
ads inside of your interface, for instance, you might have a really important
reason for your users to be in your interface and not somewhere else.

If you find yourself in the unenviable situation of having to switch your
answer from "Yes" to "No" it will mean telling people who are very interested
in your product that they can't do that with it.  It means you have to tell
those really excellent, interested, probably paying users that their efforts
are not wanted.  If you're popular enough by this point, it might even make the
news with phrases like "crackdown" and "locked out" and "unspeakable horse
violence" and you really don't want that.

## Ok, Got the message

Excellent.  If the answer to the question was "Yes" you can get on with
Googling GraphQL vs REST.  If the answer was "No" then you have a bunch of
other questions to answer about what your API should do and why do you need
one, etc.  You can work through all of that and make something that is just
right for you and for your users.  If you can clearly answer these questions,
then your legal team will write up the correct terms and conditions and your
developers will build the right API and so on down the line.  Your users might
still want more access, but that is now a feature request and not a reporter
asking you to comment about why you're so mean to your customers.

If you're a developer and someone just asked you to make an API, then consider
for a moment whether they have answered that question.  If you suspect they
haven't, point them here or ask yourself just to be sure.

There is still plenty of work to do, but if you have thought about and answered
this question then you haven't failed at the starting line and you will
hopefully be spared the pain of realizing that you failed at API design only
after you become popular enough for people to notice.
