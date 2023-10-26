// blocks
const city = 'New York City'
const logCitySkyline = () => {
  let skyscraper = 'Empire State Building';
    return 'The stars over the ' + skyscraper + ' in ' + city;
};

console.log(logCitySkyline());


// scope
const satellite = 'The Moon';
const galaxy = 'The Milky Way';
const stars = 'North Star';

const callMyNightSky = () => {
  return 'Night Sky: ' + satellite + ', ' + stars + ', and ' + galaxy;
}

console.log(callMyNightSky())