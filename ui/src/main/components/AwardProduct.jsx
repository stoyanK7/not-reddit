import Image from "next/image";

export default function AwardProduct({ price, name, image, description, color }) {
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
                action="http://localhost:8080/api/award/session" method="POST">
                <button
                    className={`${color} p-2 rounded-sm w-full`}
                    type="submit">
                Checkout
                </button>
            </form>
        </section>
    );
}
