async function analyze() {
    const spending = document.getElementById("spending").value;
    const savings = document.getElementById("savings").value;
    const cashback = document.getElementById("cashback").value;

    const response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            spending: Number(spending),
            savings: Number(savings),
            cashback: Number(cashback)
        })
    });

    const data = await response.json();

    document.getElementById("result").innerHTML = `
         Invested: ₹${data.micro_invest} <br>
         Score: ${data.growth_score} <br>
         ${data.saving_trigger} <br>
         ${data.milestone}
    `;
}