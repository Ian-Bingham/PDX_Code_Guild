const passport = require('passport');
const bcrypt = require('bcrypt');
const LocalStrategy = require('passport-local').Strategy;
const JwtStrategy = require('passport-jwt').Strategy;
const ExtractJwt = require('passport-jwt').ExtractJwt;

const User = require('./models/User');

passport.use(new JwtStrategy({
  secretOrKey: 'CHANGEMEPLEASE!',
  jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
}, async (payload, done) => {
  try {
    const user = await User.findOne({_id: payload._id});
    if(!user) return done(null, false);
    
    done(null, user);
  } catch (err) {
    done(err, false);
  }
}));

const verifyPassword = (password, passwordHash) => {
  return bcrypt.compareSync(password, passwordHash, 10);
};

passport.use(new LocalStrategy({
    usernameField: 'email',
    session: false,
  },
  async (email, password, done) => {
    try {
      const user = await User.findOne({ email });

      if(!user) return done(null, false);
      if(!verifyPassword(password, user.passwordHash)) return done(null, false);

      done(null, user);
    } catch(err) {
      return done(err);
    };
  }
));