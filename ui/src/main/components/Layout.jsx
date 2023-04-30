import Navbar from "@/components/Navbar";

export default function Layout({ children }) {
    return (
        <main
            className="content">
            <Navbar />
            {children}
        </main>
    );
}
