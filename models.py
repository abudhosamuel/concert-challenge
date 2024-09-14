from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)
    
    concerts = relationship('Concert', back_populates='band')
    
    # Returning all concerts the band has played
    def get_concerts(self):
        return self.concerts
    
    # Returning all venues the band has played at
    def venues(self):
        return {concert.venue for concert in self.concerts}
    
    # Creating a concert for the band at a venue on a given date, session must be passed
    def play_in_venue(self, venue, date, session):
        concert = Concert(date=date, band=self, venue=venue)
        session.add(concert)
        session.commit()
        
    # Returning all introductions for the concerts
    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts]
    
    # Class method to return the band with the most performances
    @classmethod
    def most_performances(cls, session):
        return session.query(cls).join(Concert).group_by(cls.id).order_by(func.count(Concert.id).desc()).first()

class Venue(Base):
    __tablename__ = 'venues'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)
    
    concerts = relationship('Concert', back_populates='venue')
    
    # Returning all concerts at the venue
    def get_concerts(self):
        return self.concerts
    
    # Returning all bands that have played at the venue
    def bands(self):
        return {concert.band for concert in self.concerts}
    
    # Find the concert on a specific date at the venue
    def concert_on(self, date):
        return next((concert for concert in self.concerts if concert.date == date), None)
    
    # Find the band that has played the most concerts at the venue
    def most_frequent_band(self):
        band_count = {}
        for concert in self.concerts:
            band_count[concert.band] = band_count.get(concert.band, 0) + 1
        return max(band_count, key=band_count.get)

class Concert(Base):
    __tablename__ = 'concerts'
    
    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    
    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')
    
    # Returning the band performing at this concert
    def get_band(self):
        return self.band
    
    # Returning the venue where the concert is taking place
    def get_venue(self):
        return self.venue
    
    # Returns True if the concert is happening in the band's hometown
    def hometown_show(self):
        return self.band.hometown == self.venue.city
    
    # Generates the introduction for the band at this concert
    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
