const formButtons = document.getElementsByClassName('hopper-commands__action-btn');

for (let item of formButtons) {
	item.addEventListener('click', event => {
		event.preventDefault();
	})
}

(async () => {
	const response = await fetch('http://localhost:8000/new_session', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({
			name: 'new name',
			kuz_place: 2,
			code: 'вправо 3',
			'creation_date': Date.now(),
			user_id: 1
		}),
	});

	const data = await response.json();

	console.log(data);
})();