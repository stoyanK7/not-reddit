import Image from "next/image";

export default function PostBody({ body, type }) {
    return (
        <>
            {type === "media" && (
                <div
                    className="relative overflow-visible h-40 w-full">
                    <Image
                        style={{ objectFit: "contain" }}
                        src={body}
                        alt="Application logo"
                        fill
                        // sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
                    />
                </div>
            )}
        </>
    );
}
