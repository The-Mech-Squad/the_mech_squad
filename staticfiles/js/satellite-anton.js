var satellite = require(['satellite.js']);

var positionAndVelocity = satellite.propagate(satrec, new Date());

var longstr1 = '1 25544U 98067A   20118.20695473  .00009244  00000-0  17373-3 0  9991';
var longstr2 = '2 25544  51.6448 240.7867 0001172 200.9317 226.8060 15.49332606224110';

var satrec = satellite.twoline2satrec(longstr1, longstr2);


var positionEci = positionAndVelocity.position,
  velocityEci = positionAndVelocity.velocity
  ;

var observerGd = {
  longitude: satellite.degreesToRadians(-122.0308),
  latitude: satellite.degreesToRadians(36.9613422),
  height: 0.370
};

var gmst = satellite.gstime(new Date());

var satelliteX = positionEci.x,
  satelliteY = positionEci.y,
  satelliteZ = positionEci.z
  ;


var longitudeStr = satellite.degreesLong(observerGd.longitude),
  latitudeStr = satellite.degreesLat(observerGd.latitude)
  ;