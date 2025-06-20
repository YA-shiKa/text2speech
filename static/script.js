document.getElementById("tts-form").addEventListener("submit", async function(e) {
  e.preventDefault();

  const text = document.getElementById("text").value;
  if (!text.trim()) {
    alert("Please enter some text!");
    return;
  }

  const formData = new FormData();
  formData.append("text", text);

  try {
    const response = await fetch("/speak", {
      method: "POST",
      body: formData
    });

    if (!response.ok) {
      alert("Failed to generate audio. Try again.");
      return;
    }

    const audioBlob = await response.blob();
    const audioUrl = URL.createObjectURL(audioBlob);
    const audioElement = document.getElementById("audio");
    audioElement.src = audioUrl;
    audioElement.play();
  } catch (err) {
    console.error("Error:", err);
    alert("Something went wrong.");
  }
});
