from db.models import db, Movie, Genre

def seed_data():
    if Genre.query.first() or Movie.query.first():
        print("Data already seeded.")
        return

    # Create Genres
    action = Genre(name="Action")
    comedy = Genre(name="Comedy")
    drama = Genre(name="Drama")
    sci_fi = Genre(name="Sci-Fi")
    horror = Genre(name="Horror")
    thriller = Genre(name="Thriller")
    romance = Genre(name="Romance")
    fantasy = Genre(name="Fantasy")
    db.session.add_all([action, comedy, drama, sci_fi, horror, thriller, romance, fantasy])
    db.session.commit()

    # Movie seed data
    movies = [
        Movie(
            name="Edge of Tomorrow",
            category="new_release",
            genres=[action, sci_fi],
            release="2025-04-01",
            rating_star="4.6",
            totalRatings="1200",
            age_rating="PG-13",
            runtime="113 mins",
            sypnosis="A soldier relives the same day in a war against aliens and becomes better each time.",
            cast="Tom Cruise, Emily Blunt",
            director="Doug Liman",
            writers="Christopher McQuarrie",
            trailer="https://www.youtube.com/watch?v=vw61gCe2oqI",
            poster="https://image.tmdb.org/t/p/original/edge_of_tomorrow.jpg"
        ),
        Movie(
            name="Laugh Factory",
            category="new_release",
            genres=[comedy],
            release="2025-03-27",
            rating_star="4.1",
            totalRatings="620",
            age_rating="PG",
            runtime="98 mins",
            sypnosis="A group of stand-up comedians try to save their favorite comedy club.",
            cast="Kevin Hart, Tiffany Haddish",
            director="Judd Apatow",
            writers="Amy Poehler",
            trailer="https://www.youtube.com/watch?v=example1",
            poster="https://image.tmdb.org/t/p/original/laugh_factory.jpg"
        ),
        Movie(
            name="Haunted Nights",
            category="new_release",
            genres=[horror, thriller],
            release="2025-03-30",
            rating_star="4.3",
            totalRatings="980",
            age_rating="R",
            runtime="105 mins",
            sypnosis="A couple moves into a haunted house with a sinister past.",
            cast="Vera Farmiga, Patrick Wilson",
            director="James Wan",
            writers="Leigh Whannell",
            trailer="https://www.youtube.com/watch?v=example2",
            poster="https://image.tmdb.org/t/p/original/haunted_nights.jpg"
        ),
        Movie(
            name="The Boom",
            category="popular",
            genres=[action],
            release="2024-12-12",
            rating_star="4.9",
            totalRatings="8900",
            age_rating="PG-13",
            runtime="121 mins",
            sypnosis="A vigilante hero rises in a crime-ridden metropolis.",
            cast="Chris Hemsworth, Scarlett Johansson",
            director="Michael Bay",
            writers="Zack Snyder",
            trailer="https://www.youtube.com/watch?v=example3",
            poster="https://image.tmdb.org/t/p/original/the_boom.jpg"
        ),
        Movie(
            name="Romantic Reboot",
            category="popular",
            genres=[romance, comedy],
            release="2024-11-05",
            rating_star="4.7",
            totalRatings="7800",
            age_rating="PG",
            runtime="103 mins",
            sypnosis="Two exes meet again thanks to a dating app with a twist.",
            cast="Ryan Gosling, Emma Stone",
            director="Nancy Meyers",
            writers="Greta Gerwig",
            trailer="https://www.youtube.com/watch?v=example4",
            poster="https://image.tmdb.org/t/p/original/romantic_reboot.jpg"
        ),
        Movie(
            name="Alien City",
            category="popular",
            genres=[sci_fi, action],
            release="2024-09-18",
            rating_star="4.5",
            totalRatings="6500",
            age_rating="PG-13",
            runtime="117 mins",
            sypnosis="A city hides the truth about its alien inhabitants.",
            cast="Zendaya, Oscar Isaac",
            director="Denis Villeneuve",
            writers="Charlie Brooker",
            trailer="https://www.youtube.com/watch?v=example5",
            poster="https://image.tmdb.org/t/p/original/alien_city.jpg"
        ),
        Movie(
            name="Undercover Joy",
            category="recommended",
            genres=[comedy, drama],
            release="2024-08-10",
            rating_star="4.3",
            totalRatings="1100",
            age_rating="PG",
            runtime="101 mins",
            sypnosis="A depressed detective finds joy while going undercover in a theater troupe.",
            cast="Paul Rudd, Mindy Kaling",
            director="Taika Waititi",
            writers="Phoebe Waller-Bridge",
            trailer="https://www.youtube.com/watch?v=example6",
            poster="https://image.tmdb.org/t/p/original/undercover_joy.jpg"
        ),
        Movie(
            name="Code Zero",
            category="recommended",
            genres=[sci_fi, action],
            release="2024-07-14",
            rating_star="4.4",
            totalRatings="1330",
            age_rating="PG-13",
            runtime="108 mins",
            sypnosis="A hacker discovers a secret AI controlling the world’s data.",
            cast="John Boyega, Anya Taylor-Joy",
            director="Alex Garland",
            writers="Lisa Joy",
            trailer="https://www.youtube.com/watch?v=example7",
            poster="https://image.tmdb.org/t/p/original/code_zero.jpg"
        ),
        Movie(
            name="Dreamscape",
            category="recommended",
            genres=[drama, fantasy],
            release="2024-06-01",
            rating_star="4.2",
            totalRatings="900",
            age_rating="PG",
            runtime="99 mins",
            sypnosis="A teen can enter other people’s dreams, but loses grip on reality.",
            cast="Millie Bobby Brown, Jacob Tremblay",
            director="Lana Wachowski",
            writers="Neil Gaiman",
            trailer="https://www.youtube.com/watch?v=example8",
            poster="https://image.tmdb.org/t/p/original/dreamscape.jpg"
        ),
        Movie(
            name="Fear Street",
            category="recommended",
            genres=[horror, drama],
            release="2024-05-25",
            rating_star="4.0",
            totalRatings="720",
            age_rating="R",
            runtime="102 mins",
            sypnosis="A cursed town faces its past when teens uncover a dark ritual.",
            cast="Sadie Sink, Finn Wolfhard",
            director="Leigh Janiak",
            writers="R.L. Stine",
            trailer="https://www.youtube.com/watch?v=example9",
            poster="https://image.tmdb.org/t/p/original/fear_street.jpg"
        ),
    ]

    db.session.add_all(movies)
    db.session.commit()
    print("Seeded 10 detailed movies across categories.")
