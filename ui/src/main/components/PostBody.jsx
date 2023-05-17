import Image from "next/image";

import loaderProp from "@/utils/loaderProp";

export default function PostBody({ body, type }) {
    return (
        <>
            {type === "media" && (
                <div
                    className="relative overflow-visible h-40 w-full">
                    <Image
                        style={{ objectFit: "contain" }}
                        src={`${process.env.NEXT_PUBLIC_API_SERVICE_URL}/api/post/media/${body}`}
                        alt="Application logo"
                        fill
                        loader={loaderProp}
                        // sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
                    />
                </div>
            )}
            {type === "text" && (
                <div>
                    {body}
                </div>
            )}
        </>
    );
}
