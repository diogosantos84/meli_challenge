db = db.getSiblingDB('meli_challenge');
db.createUser({
    user: 'meli_challenge',
    pwd: 'MELI123',
    roles: [
      {
        role: 'readWrite',
        db: 'meli_challenge'
      }
    ]
  })