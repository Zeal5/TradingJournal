import "../styles/globals.css";
import Layout from "../components/layouts";



function MyApp({ Component, pageProps }) {
  if(Component.getLayout){
    return Component.getLayout(<Component {...pageProps} />)
  }
  else{
  return (
    <Layout>
      <Component {...pageProps} />
    </Layout>
  )}
}

export default MyApp;
