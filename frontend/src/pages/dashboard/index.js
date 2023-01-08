import Head from "next/head";
import styles from "../../styles/dashboard/dashboard.module.css";
import { useRouter } from "next/router";
import Footer from "../../components/Footer";

export default function Home({ data }) {
  // console.log("data: >> ", data);
  // console.log("doneL >>", done);
  const router = useRouter();


  const navigateTrade = ({ slug }) => {
    // if (typeof window === "undefined") return null;
    router.push('dashboard/'+slug);
    
  };
  return (
    <div className={styles.container}>
      <Head>
        <title>DashBoard</title>
      </Head>

      <table className={styles.table}>
        <thead>
          <tr>
            <th className={styles.th}>id</th>
            <th className={styles.th}>title</th>
            <th className={styles.th}>price</th>
            <th className={styles.th}>sale-price 20%-off</th>
          </tr>
        </thead>
        <tbody>
          {data.map((element) => (
            <tr key={element.slug} onClick={() => navigateTrade(element)}>
              <td className={styles.td}>{element.pk}</td>
              <td className={styles.td}>{element.title}</td>
              <td className={styles.td}>{element.price}</td>
              <td className={styles.td}>{element.sale_price}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
export async function getStaticProps() {
  const response = await fetch(`${process.env.BASE_URL}/products/`);

  const data = await response.json();
  return {
    props: {
      data: data,
      dont: true,
    },
  };
}

Home.getLayout = function PageLayout(page){
  return (
    <>
    {page}
    <Footer />
    </>
  )
}