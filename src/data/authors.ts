import marioImage from "../assets/authors/robi.png";

export interface Props {
  name: string;
  slug: string;
  image: string;
  bio: string;
}

export type Author = Props;

export const authors: Props[] = [
  {
    name: "Robi Maulana",
    slug: "robi-maulana",
    image: marioImage,
    bio: "Kalau sedang tidak mengerjakan apa-apa, Robi mengerjakan apa-apa di sini. Kalau sedang tidak mengerjakan apa-apa di sini, Robi mengerjakan apa-apa di sini.",
  },
];
