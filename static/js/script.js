let isMicActive = false;
let isCameraActive = false;
let mediaStream = null;

let mediaRecorder;
let audioChunks = [];
let recordingTimeout;
let elapsedTime = 0;
let timerInterval;

let audioUrl;
let photoUrl;
let file;

function insertSymbol(symbol) {
  const textarea = document.getElementById("math_text");
  const cursorPos = textarea.selectionStart;

  const textBefore = textarea.value.substring(0, cursorPos);
  const textAfter = textarea.value.substring(cursorPos);
  textarea.value = textBefore + symbol + textAfter;

  textarea.selectionStart = cursorPos + symbol.length;
  textarea.selectionEnd = cursorPos + symbol.length;
  textarea.focus();
}

function toggleKeyboard() {
  const keyboard = document.getElementById("math_keyboard");
  keyboard.style.display = keyboard.style.display === "grid" ? "none" : "grid";
}

// Klavye dışında bir yere tıklandığında klavyeyi kapatma
document.addEventListener("click", function (event) {
  const keyboard = document.getElementById("math_keyboard");
  const keyboardBtn = document.getElementById("keyboardBtn");

  if (!keyboard.contains(event.target) && event.target !== keyboardBtn) {
    keyboard.style.display = "none";
  }
});

function toggleMicrophonePopup() {
  document.getElementById("microphone_popup").classList.toggle("hidden");
}

function toggleMicrophone() {
  const micButton = document.getElementById("start_recording");
  if (!isMicActive) {
    micButton.classList.remove("bg-green-500");
    micButton.classList.add("bg-red-500");
    micButton.innerHTML = "Kaydı Durdur";
    startRecording();
  } else {
    stopRecording();
    micButton.classList.remove("bg-red-500");
    micButton.classList.add("bg-green-500");
    micButton.innerHTML = "Kaydı Başlat";
  }
}

async function startRecording() {
  audioChunks = [];
  elapsedTime = 0;
  updateTimerDisplay();

  try {
    mediaStream = await navigator.mediaDevices.getUserMedia({
      audio: true,
    });
    mediaRecorder = new MediaRecorder(mediaStream);

    mediaRecorder.ondataavailable = (event) => {
      audioChunks.push(event.data);
    };

    mediaRecorder.onstop = () => {
      saveAudio();
    };

    mediaRecorder.start();
    isMicActive = true;

    // Başlatılan zamanlayıcı her saniye güncellensin
    timerInterval = setInterval(() => {
      elapsedTime++;
      updateTimerDisplay();
    }, 1000);

    // 20 saniye sonra kaydı otomatik olarak durdu
    recordingTimeout = setTimeout(() => {
      stopRecording();
    }, 20000);
  } catch (error) {
    console.error("Ses kaydedilemiyor:", error);
  }
}

function stopRecording() {
  if (mediaRecorder && mediaRecorder.state !== "inactive") {
    mediaRecorder.stop();
  }
  if (mediaStream) {
    mediaStream.getTracks().forEach((track) => track.stop());
  }
  clearInterval(timerInterval); // Zamanlayıcı durdurulsun
  clearTimeout(recordingTimeout);
  isMicActive = false;
}

function saveAudio() {
  const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
  audioUrl = URL.createObjectURL(audioBlob);
  console.log("Kaydedilen ses:", audioUrl);

  // Kaydedilen sesi sunucuya gönderme kodunu buraya ekleyebilirsiniz

  // Ses önizleme alanını göster
  const audioPreview = document.getElementById("audio_preview");
  audioPreview.src = audioUrl;
  document.getElementById("audio_preview_container").classList.remove("hidden");
  document.getElementById("solution_preview").classList.remove("hidden");
}

function updateTimerDisplay() {
  const timerDisplay = document.getElementById("timer_display");
  timerDisplay.innerText = `Geçen Zaman: ${elapsedTime} / 20 saniye`;
}

function discardRecording() {
  audioChunks = [];
  elapsedTime = 0;
  updateTimerDisplay();
  toggleMicrophonePopup();
}

async function toggleCamera() {
  if (!isCameraActive) {
    mediaStream = await navigator.mediaDevices.getUserMedia({
      video: true,
    });
    document.getElementById("camera_view").srcObject = mediaStream;
    document.getElementById("camera_popup").classList.remove("hidden");
    isCameraActive = true;
  }
}

function closeCamera() {
  if (mediaStream) {
    mediaStream.getTracks().forEach((track) => track.stop());
  }
  document.getElementById("camera_popup").classList.add("hidden");
  isCameraActive = false;
}

function capturePhoto() {
  const videoElement = document.getElementById("camera_view");
  const canvas = document.createElement("canvas");
  canvas.width = videoElement.videoWidth;
  canvas.height = videoElement.videoHeight;
  const context = canvas.getContext("2d");
  context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
  photoUrl = canvas.toDataURL("image/jpeg");

  //Sunucuya fotoğraf gönderme kodu buraya eklenebilir Fotograf ile ilgili islemler buraya eklenebilir

  // Fotoğraf önizleme alanını göster
  const photoPreview = document.getElementById("photo_preview");
  photoPreview.src = photoUrl;
  document.getElementById("photo_preview_container").classList.remove("hidden");
  document.getElementById("solution_preview").classList.remove("hidden");

  closeCamera();
}

function handleFileSelect(event) {
  const file = event.target.files[0];
  if (
    file &&
    (file.type === "image/jpeg" ||
      file.type === "image/jpg" ||
      file.type === "image/png")
  ) {
    const reader = new FileReader();
    reader.onload = (e) => {
      document.getElementById("file_preview").src = e.target.result;
      document
        .getElementById("file_preview_container")
        .classList.remove("hidden");
    };
    reader.readAsDataURL(file);

    // OCR işlemi için API'ye gönder
    const formData = new FormData();
    formData.append("image", file);

    fetch("http://127.0.0.1:5000/extract-text", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        document.getElementById("math_text").value = data.text;
      })
      .catch((error) => {
        console.error("OCR API Hatası:", error);
      });
  } else {
    alert("Lütfen yalnızca .jpg, .jpeg veya .png formatında bir dosya seçin.");
  }
}

function removeFilePreview() {
  document.getElementById("file_preview").src = "";
  document.getElementById("file_input").value = "";
  document.getElementById("file_preview_container").classList.add("hidden");
}

function removeAudioPreview() {
  const audioPreviewContainer = document.getElementById(
    "audio_preview_container"
  );
  audioPreviewContainer.classList.add("hidden");

  // Eğer hem ses hem de fotoğraf önizlemesi kapatılmışsa genel önizleme alanını da gizle
  if (
    document
      .getElementById("photo_preview_container")
      .classList.contains("hidden")
  ) {
    document.getElementById("solution_preview").classList.add("hidden");
  }
}

function removePhotoPreview() {
  const photoPreviewContainer = document.getElementById(
    "photo_preview_container"
  );
  photoPreviewContainer.classList.add("hidden");

  // Eğer hem ses hem de fotoğraf önizlemesi kapatılmışsa genel önizleme alanını da gizle
  if (
    document
      .getElementById("audio_preview_container")
      .classList.contains("hidden")
  ) {
    document.getElementById("solution_preview").classList.add("hidden");
  }
}

async function submitSolution() {
  // Girdi elemanlarını al
  const mathTerm = document.getElementById("math_text").value;
  const fileInput = file;
  const audio = audioUrl; // Ses URL'si veya Blob olarak kullanabilirsiniz
  const photo = photoUrl; // Fotoğraf URL'si veya Blob olarak kullanabilirsiniz

  // Gönderim verilerini hazırla
  const formData = new FormData();

  // Math Text varsa ekle
  if (mathTerm) {
    formData.append("math_term", mathTerm);
  }

  // Dosya yüklendiyse ekle
  if (fileInput) {
    formData.append("file", fileInput);
  }

  // Ses kaydı varsa ekle
  if (audioUrl) {
    formData.append("audio", audio);
  }

  // Fotoğraf çekildiyse ekle
  if (photoUrl) {
    formData.append("photo", photo);
  }

  try {
    // Çözüm isteği gönder
    const response = await fetch("/solve", {
      method: "POST",
      body: formData,
    });

    // Yanıt başarılıysa verileri ekrana yerleştir
    if (response.ok) {
      const data = await response.json();

      // Doküman ve Videolar Bölümünü Göster
      document.getElementById("document_section").classList.remove("hidden");
      document.getElementById("videos_section").classList.remove("hidden");

      document.getElementById("solution_text").innerHTML = data.solution;
      document.getElementById("explanation_text").innerText = data.explanation;
      document.getElementById("video_1").src = data.videos[0];
      document.getElementById("video_2").src = data.videos[1];
      document.getElementById("video_3").src = data.videos[2];
    } else {
      console.error("Çözüm alınamadı:", await response.text());
    }
  } catch (error) {
    console.error("Bir hata oluştu:", error);
  }
}
