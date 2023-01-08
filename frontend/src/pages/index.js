import Head from "next/head";
import styles from "../styles/index.module.css";

export default function Home() {
  return (
    <div className={styles.body}>
      <Head>
        <title>Home</title>
      </Head>
      <div className={styles.welcome}>Welcome To Home Page</div>

      <div className={styles.maintext}>
        Welcome to [Trading Journal], the ultimate trading companion that helps
        you turn your trading dreams into reality. Our beautifully designed
        website offers a wealth of features that make it easy for you to track,
        analyze, and improve your trading performance. With [Trading Journal],
        you can effortlessly record and review all of your trades, including
        detailed notes and analysis. This helps you identify strengths and
        weaknesses, and make informed decisions to boost your profits. In
        addition to trade tracking, [Trading Journal] also provides a range of
        powerful tools and resources to help you succeed. These include
        real-time market data, customizable alerts, and in-depth market insights
        from our team of trading experts. But [Trading Journal] isn't just about
        numbers and stats. We believe that trading should be an enjoyable and
        fulfilling experience, which is why we've included features such as
        customizable themes and a motivational quote of the day to keep you
        inspired. So why wait? Start using [Trading Journal] today and take your
        trading to new heights!
      </div>
    </div>
  );
}
