const randomImages = document.getElementById("random-images");

const urlUnsplashBase = "https://api.unsplash.com";
const imagesSizes = [800, 900, 500, 801, 904, 505];

const loadEnv = async () => {
  const envVariables = {};

  const response = await fetch("./.env");
  const envText = await response.text();

  envText.split("\n").forEach((line) => {
    const [key, value] = line
      .split("=")
      .map((item) => item.trim().replaceAll('"', ""));
    if (key && value) {
      envVariables[key] = value;
    }
  });

  return envVariables;
};

const mountImage = (src) => {
  const div = document.createElement("div");
  const img = document.createElement("img");

  div.classList.add("image-gallery");

  img.src = src;
  img.alt = "Random Image";

  div.appendChild(img);

  return div;
};

const getRandomImageUnsplash = async () => {
  const response = loadEnv().then(async (env) => {
    const response = await fetch(
      `${urlUnsplashBase}/photos/random?client_id=${env.UNSPLASH_ACCESS_KEY}&count=6`
    );

    return await response.json();
  });

  return await response;
};

const showImages = async () => {
  const unsplashImages = await getRandomImageUnsplash();

  unsplashImages.forEach((image, key) => {
    const imageUrl = `${image.urls.full}&w=${imagesSizes[key]}&h=${imagesSizes[key]}`;

    const mount = mountImage(imageUrl);

    randomImages.appendChild(mount);
  });
};

showImages();
