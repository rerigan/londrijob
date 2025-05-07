
import "./globals.css";




export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <title>LondriJob - Vagas em Londrina</title>
      <body
        className={`antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
