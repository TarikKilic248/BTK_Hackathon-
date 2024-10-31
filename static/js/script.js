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


async function startRecording() {
  audioChunks = [];
  elapsedTime = 0;
  updateTimerDisplay();

  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream, {
      mimeType: 'audio/webm' // Web tarayıcıları genelde webm formatını destekler
    });

    mediaRecorder.ondataavailable = (event) => {
      audioChunks.push(event.data);
    };

    mediaRecorder.onstop = () => {
      saveAudio();
    };

    mediaRecorder.start();
    isMicActive = true;

    timerInterval = setInterval(() => {
      elapsedTime++;
      updateTimerDisplay();
    }, 1000);

    recordingTimeout = setTimeout(() => {
      stopRecording();
    }, 20000);
  } catch (error) {
    console.error("Ses kaydedilemiyor:", error);
  }
}

async function saveAudio() {
  try {
    // WebM formatındaki ses verilerini WAV formatına dönüştür
    const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
    
    // Dosya adı için timestamp oluştur
    const timestamp = new Date().toISOString().replace(/[:.]/g, "-");
    const fileName = `recording-${timestamp}.wav`;
    
    // FormData oluştur
    const formData = new FormData();
    formData.append("audio", audioBlob, fileName);

    // Backend'e gönder
    const response = await fetch("/save-audio", {
      method: "POST",
      body: formData
    });

    const data = await response.json();

    if (data.success) {
      console.log("Ses kaydı başarıyla kaydedildi:", data.filepath);
      
      // Ses önizleme alanını güncelle ve göster
      const audioPreview = document.getElementById("audio_preview");
      audioPreview.src = `/audios/${data.filename}`;
      document.getElementById("audio_preview_container").classList.remove("hidden");
      document.getElementById("solution_preview").classList.remove("hidden");

      // solve endpointine ses dosyası yolunu gönder
      const solveFormData = new FormData();
      solveFormData.append("audio_path", data.filepath);
      
      const solveResponse = await fetch("/solve", {
        method: "POST",
        body: solveFormData
      });

      const solveData = await solveResponse.json();
      
      // Çözüm sonuçlarını göster
      if (solveData.solution) {
        document.getElementById("solution_text").innerHTML = solveData.solution;
        document.getElementById("explanation_text").innerText = solveData.explanation;
        // Video önizlemelerini güncelle
        if (solveData.videos) {
          document.getElementById("video_1").src = solveData.videos[0];
          document.getElementById("video_2").src = solveData.videos[1];
          document.getElementById("video_3").src = solveData.videos[2];
        }
      }
    } else {
      console.error("Ses kaydı kaydedilemedi:", data.error);
    }
  } catch (error) {
    console.error("Ses kaydı işlenirken hata oluştu:", error);
  }
}

function stopRecording() {
  if (mediaRecorder && mediaRecorder.state !== "inactive") {
    mediaRecorder.stop();
    const tracks = mediaRecorder.stream.getTracks();
    tracks.forEach(track => track.stop());
  }
  clearInterval(timerInterval);
  clearTimeout(recordingTimeout);
  isMicActive = false;
}

function discardRecording() {
  stopRecording();
  audioChunks = [];
  elapsedTime = 0;
  updateTimerDisplay();
  document.getElementById("audio_preview_container").classList.add("hidden");
  document.getElementById("solution_preview").classList.add("hidden");
  toggleMicrophonePopup();
}

function updateTimerDisplay() {
  const timerDisplay = document.getElementById("timer_display");
  timerDisplay.innerText = `Geçen Zaman: ${elapsedTime} / 20 saniye`;
}

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



<<<<<<< HEAD
=======
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

  // FormData ile dosyayı 'file' anahtarıyla ekleyin
  const formData = new FormData();
  formData.append("file", audioBlob, "audio.wav");

  fetch('/upload-audio', {
    method: 'POST',
    body: formData,
  }).then(response => {
    if (response.ok) {
      console.log("Ses başarıyla yüklendi.");
    } else {
      console.error("Ses yüklenirken hata oluştu.");
    }
  });

  // Ses önizleme alanını göster
  const audioPreview = document.getElementById("audio_preview");
  audioPreview.src = audioUrl;
  document.getElementById("audio_preview_container").classList.remove("hidden");
  document.getElementById("solution_preview").classList.remove("hidden");
}
>>>>>>> 8b2411af122e84a38d64d2b71d79f2782d181271

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
