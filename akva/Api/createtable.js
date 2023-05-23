const connection = require('./db');

(async function createTables() {
    try {
        let res = connection.none(`CREATE TABLE userCount 
            (
                id SERIAL PRIMARY KEY,
                name VARCHAR(40) NOT NULL,
                count VARCHAR(40) NOT NULL
            );`);
    } catch (err) {
        console.error(err);
    }

})();