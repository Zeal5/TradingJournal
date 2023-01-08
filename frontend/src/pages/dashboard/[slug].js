import React from 'react';
import { useRouter } from "next/router";
import styles from "../../styles/dashboard/slugs.module.css"

export default function Trade({ data }) {
  const {query:slug} = useRouter()

  return (
   
    <div className={styles.body}>
     {data.pk}
     
    </div>
  )
}

export async function getStaticPaths() {
  const response = await fetch(`${process.env.BASE_URL}/products/`);

  const data = await response.json();

  const allSlugs = data.map(item => item.slug)
  const paths = allSlugs.map(slug=> ({params: {slug: slug}}))

  return {
    paths,
    fallback:false
  }
    }
export async function getStaticProps({ params }) {
  const response = await fetch(`${process.env.BASE_URL}/products/${params.slug}`);

  const data = await response.json();
  return{
    props:{
      data
    }
  }
}