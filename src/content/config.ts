import { z, defineCollection } from "astro:content";

const commonSchema = ({ image }) =>
  z.object({
    title: z.string(),
    excerpt: z.string(),
    category: z.string().trim(),
    author: z.string().trim(),
    draft: z.boolean().optional(),
    tags: z.array(z.string()),
    image: image(),
    publishDate: z.string().transform((str) => new Date(str)),
  });

const BlogPosts = defineCollection({
  schema: commonSchema,
});

const KamusPsikologiOnline = defineCollection({
  schema: commonSchema,
});

const SkripsiPsikologi = defineCollection({
  schema: commonSchema,
});

const TesKepribadian = defineCollection({
  schema: commonSchema,
});

export const collections = {
  blog: BlogPosts,
  kamuspsikologionline: KamusPsikologiOnline,
  skripsipsikologi: SkripsiPsikologi,
  teskepribadian: TesKepribadian,
};
