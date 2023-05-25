import { useEffect } from "react";
import { toast } from "react-toast";

import AwardProduct from "@/components/AwardProduct";

export default function Award() {
    useEffect(() => {
        const query = new URLSearchParams(window.location.search);

        if (query.get("success")) {
            toast.success("Order placed! You will receive an email confirmation.");
        }

        if (query.get("canceled")) {
            toast.info("Order canceled -- continue to shop around and checkout when you're ready.");
        }
    }, []);
    return (
        <main
            className="flex flex-col w-screen h-screen justify-center items-center">
            <div
                className="flex gap-2">
                <AwardProduct
                    name="Silver Award"
                    description="A silver award for the best of the best"
                    price="1.50"
                    image="silver-award.png"
                    color="bg-gray-300 hover:bg-gray-500 transition ease-in-out" />
                <AwardProduct
                    name="Gold Award"
                    description="A gold award for the best of the best"
                    price="3.00"
                    image="gold-award.png"
                    color="bg-yellow-300 hover:bg-yellow-500 transition ease-in-out" />
                <AwardProduct
                    name="Platinum Award"
                    description="A silver award for the best of the best"
                    price="5.00"
                    image="platinum-award.png"
                    color="bg-teal-200 hover:bg-teal-400 transition ease-in-out" />
            </div>
        </main>
    );
}
