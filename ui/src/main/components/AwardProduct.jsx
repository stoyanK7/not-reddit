import Image from "next/image";
import { useRouter } from "next/router";

import fromApi from "@/utils/fromApi";

export default function AwardProduct({ type, price, name, image, description, color }) {
    const router = useRouter();

    return (
        <section
            className="bg-white p-4 rounded-sm shadow-reddit">
            <div
                className="text-center">
                <div
                    className="relative overflow-visible w-40 h-20 hover:cursor-pointer">
                    <Image
                        style={{ objectFit: "contain" }}
                        src={`/${image}`}
                        alt={description}
                        fill />
                </div>
                <div
                    className="description">
                    <h3
                        className="font-bold">{name}</h3>
                    <h5
                        className="italic">&euro;{price}</h5>
                </div>
            </div>
            <form
                action={fromApi("/api/award/session")}
                method="POST">
                <input
                    name="subject_type"
                    value={router.query.subject_type}
                    hidden />
                <input
                    name="award_type"
                    value={type}
                    hidden />
                <input
                    name="subject_id"
                    value={router.query.subject_id}
                    hidden />
                <button
                    className={`${color} p-2 rounded-sm w-full`}
                    type="submit">
                Checkout
                </button>
            </form>
        </section>
    );
}
