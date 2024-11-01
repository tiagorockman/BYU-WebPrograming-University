using System;

class Program
{
    static void Main(string[] args)
    {
        List<Video> videos = new();
        User user1 = new User("James");
        User user2 = new User("Paty");
        User user3 = new User("Macconel");

        Video video1 = new Video("Cooking popcorn", "Victor Cook", 563);
        video1.StoreComment(new Comment("I never knew making popcorn could be this fun! Definitely trying this recipe tonight.", user1.GetUserName()));
        video1.StoreComment(new Comment("The tips you gave were so helpful! Mine always burns, but this turned out perfect.", user2.GetUserName()));
        video1.StoreComment(new Comment("Love how you made it so simple and easy to follow. Subscribed for more cooking videos!", user3.GetUserName()));
        video1.StoreComment(new Comment("I tried adding some extra butter like you suggested, and it was AMAZING!", user3.GetUserName()));
        videos.Add(video1);

        Video video2 = new Video("Playing HalfCourt Basketball", "SlamDunk", 945);
        video2.StoreComment(new Comment("That half-court shot at the end was insane! How many tries did it take?", user1.GetUserName()));
        video2.StoreComment(new Comment("I wish I could ball like that! Great video and awesome skills.", user2.GetUserName()));
        video2.StoreComment(new Comment("Can you do a tutorial on your dribbling moves next? Those were slick!", user3.GetUserName()));
        video2.StoreComment(new Comment("Love the energy in this video, makes me want to hit the court now.", user1.GetUserName()));
        videos.Add(video2);

        Video video3 = new Video("Traveling to Florida from Brazil", "WorldTrip channel", 1056);
        video3.StoreComment(new Comment("I loved seeing the sights along the way! Definitely adding Florida to my travel list.", user1.GetUserName()));
        video3.StoreComment(new Comment("What an amazing journey! Your travel vlogs are always so immersive.", user2.GetUserName()));
        video3.StoreComment(new Comment("Brazil to Florida, what a trip! The beaches there look incredible.", user3.GetUserName()));
        video3.StoreComment(new Comment("The way you captured the experience makes me feel like I was there with you!", user3.GetUserName()));
        videos.Add(video3);

        Video video4 = new Video("English Video React", "Bruna's Channel", 320);
        video4.StoreComment(new Comment("Haha, your reaction was priceless! I had the same thoughts when I watched this.", user1.GetUserName()));
        video4.StoreComment(new Comment("I love your sense of humor! Can't wait for your next reaction video.", user2.GetUserName()));
        video4.StoreComment(new Comment("Bruna, you're so relatable! I was laughing along with you the whole time.", user3.GetUserName()));
        video4.StoreComment(new Comment("Great reaction! It’s always fun to see videos from another perspective.", user2.GetUserName()));
        videos.Add(video4);

        foreach(var v in videos){
            Console.WriteLine($"\n{v.DisplayVideo()}");
            Console.WriteLine("Comments:");
            foreach(var c in v.GetComments())
               Console.WriteLine(c.DisplayComment());

        }

    }


}