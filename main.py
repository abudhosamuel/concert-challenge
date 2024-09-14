from database_setup import session
from models import Band, Venue, Concert

# Create some instances of Bands and Venues
band1 = Band(name="The Rolling Stones", hometown="London")
band2 = Band(name="Coldplay", hometown="London")

venue1 = Venue(title="Wembley Stadium", city="London")
venue2 = Venue(title="Madison Square Garden", city="New York")

# Add them to the session and commit to the database
session.add_all([band1, band2, venue1, venue2])
session.commit()

# Test Band playing in Venue (create a concert)
band1.play_in_venue(venue1, "2024-09-01", session)  # Pass session here
band2.play_in_venue(venue2, "2024-09-02", session)  # Pass session here
session.commit()

# Test querying data
print(f"{band1.name} has performed at the following venues:")
for venue in band1.venues():
    print(f"- {venue.title} in {venue.city}")

print(f"{venue1.title} has hosted the following bands:")
for band in venue1.bands():
    print(f"- {band.name} from {band.hometown}")

# Test Concert introduction and hometown show
concert1 = session.query(Concert).filter_by(band_id=band1.id).first()
print(concert1.introduction())  # Should print: Hello London!!!!! We are The Rolling Stones and we're from London
print(f"Is it a hometown show? {concert1.hometown_show()}")  # Should return True since both concert and band are in London

# Test Band most performances
most_performances_band = Band.most_performances(session)
print(f"The band with the most performances is: {most_performances_band.name}")
