const express = require('express');
const router = express.Router();
const connection = require('../db');


router.get('/', async (req, res) => {
	try {
		let rows = connection.manyOrNone(`SELECT * FROM userCount ORDER BY count DESC;`);
		res.send(await rows);
	} catch (err) {
		console.error(err);
	}
});

router.get('/:name', async (req, res) => {
	try {
		let rows = connection.oneOrNone(
			`SELECT * FROM userCount WHERE name = $1;`,
			[req.params.name]);
			
		if (await rows == null){
			res.send([]);
		} else {
			res.send(await rows);
		}
		

	} catch (err) {
		console.error(err);
	}
});

router.post('/', async (req, res) => {
	
	try {
		let rows = connection.one(
			`INSERT INTO userCount (name, count) 
			VALUES ($1, $2) 
			RETURNING id, name, count;`,
			[req.body.name, req.body.count]);
		res.send(await rows);
	} catch (err) {
		console.error(err);
	}
});

router.put('/:name', async (req, res) => {
	try {
		let rows = connection.none(
			`UPDATE userCount SET count = $2 WHERE name = $1`,
			[req.body.name, req.body.count]
		);
		res.sendStatus(200);
	} catch (err) {
		console.error(err);
	}
});

router.delete('/:id', async (req, res) => {
	try {
		let rows = connection.none(
			`DELETE FROM userCount WHERE id = $1`,
			[+req.params.id]
		);
		res.sendStatus(200);
	} catch (err) {
		console.error(err);
	}
});

module.exports = router;