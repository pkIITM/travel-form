document.getElementById('travelForm').addEventListener('submit', function(e) {
  e.preventDefault();

  // Collect form data
  const data = {
    name: document.getElementById('name').value,
    age: document.getElementById('age').value,
    phone: document.getElementById('phone').value,
    query: document.getElementById('query').value,
    destination: document.getElementById('destination').value,
  };

  // Display data on the page
  displayData(data);

  // Send data to backend
  fetch('http://localhost:5000/submit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
  .then(response => response.json())
  .then(result => {
    document.getElementById('responseMessage').textContent = result.message;
  })
  .catch(error => {
    console.error('Error:', error);
    document.getElementById('responseMessage').textContent = 'Submission failed!';
  });
});

function displayData(data) {
  const displayDiv = document.getElementById('displayData');
  displayDiv.innerHTML = `
    <h3>Submitted Data:</h3>
    <p><strong>Name:</strong> ${data.name}</p>
    <p><strong>Age:</strong> ${data.age}</p>
    <p><strong>Phone:</strong> ${data.phone}</p>
    <p><strong>Query:</strong> ${data.query}</p>
    <p><strong>Destination:</strong> ${data.destination}</p>
  `;
}