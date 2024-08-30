// async function registerUser() {
//     const name = document.getElementById('regName').value;
//     const email = document.getElementById('regEmail').value;
//     const password = document.getElementById('regPassword').value;
    
//     const response = await fetch('http://localhost:5000/register', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ name, email, password })
//     });
//     const data = await response.json();
//     alert(data.message);
// }

// async function addRestaurant() {
//     const name = document.getElementById('restName').value;
//     const location = document.getElementById('restLocation').value;
//     const hours = document.getElementById('restHours').value;
    
//     const response = await fetch('http://localhost:5000/restaurants', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ name, location, hours })
//     });
//     const data = await response.json();
//     alert(data.message);
// }

// async function addMenuItem() {
//     const restaurantId = document.getElementById('restId').value;
//     const name = document.getElementById('itemName').value;
//     const description = document.getElementById('itemDescription').value;
//     const price = document.getElementById('itemPrice').value;
    
//     const response = await fetch(`http://localhost:5000/restaurants/${restaurantId}/menu`, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ name, description, price })
//     });
//     const data = await response.json();
//     alert(data.message);
// }

// async function createOrder() {
//     const userId = document.getElementById('userId').value;
//     const restaurantId = document.getElementById('orderRestId').value;
//     const totalPrice = document.getElementById('orderTotal').value;
    
//     const response = await fetch('http://localhost:5000/orders', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ user_id: userId, restaurant_id: restaurantId, total_price: totalPrice })
//     });
//     const data = await response.json();
//     alert(data.message);
// }
