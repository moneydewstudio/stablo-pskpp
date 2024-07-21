export interface Props {
  title: string;
  slug: string;
  color: "green" | "blue" | "orange" | "pink";
  description: string;
}
export type Category = Props;

export const categories: Props[] = [
  {
    title: "Belajar Psikologi",
    slug: "belajar-psikologi",
    color: "blue",
    description: "Belajar memahami diri sendiri bisa dimulai dari sini.",
  },
  {
    title: "Kamus Psikologi Online",
    slug: "kamus-psikologi-online",
    color: "orange",
    description: "Istilah-istilah di psikologi dijelaskan di sini.",
  },
  {
    title: "Tes Kepribadian Online",
    slug: "tes-kepribadian-online",
    color: "green",
    description: "Kamu orangnya kayak apa sih? Coba kepoin di sini.",
  },
  {
    title: "Artikel Psikologi",
    slug: "artikel-psikologi",
    color: "pink",
    description:
      "Penelitian psikologi, buku psikologi, dan remeh temeh ada di sini.",
  },
];
