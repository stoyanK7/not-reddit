import Image from "next/image";

export default function AwardsBar({    silverAwards, goldAwards, platinumAwards }) {
    return (
        <div
            className="flex gap-2">
            {silverAwards > 0 && (
                <div
                    className="flex gap-2">
                    <div
                        className="relative overflow-visible w-5 h-5 hover:cursor-pointer">
                        <Image
                            style={{ objectFit: "contain" }}
                            src="/silver-award.png"
                            alt="Silver Award"
                            fill />
                    </div>
                    <span>{silverAwards}</span>
                </div>
            )}
            {goldAwards > 0 && (
                <div
                    className="flex gap-2">
                    <div
                        className="relative overflow-visible w-5 h-5 hover:cursor-pointer">
                        <Image
                            style={{ objectFit: "contain" }}
                            src="/gold-award.png"
                            alt="Gold Award"
                            fill />
                    </div>
                    <span>{goldAwards}</span>
                </div>
            )}
            {platinumAwards > 0 && (
                <div
                    className="flex gap-2">
                    <div
                        className="relative overflow-visible w-5 h-5 hover:cursor-pointer">
                        <Image
                            style={{ objectFit: "contain" }}
                            src="/platinum-award.png"
                            alt="Platinum Award"
                            fill />
                    </div>
                    <span>{platinumAwards}</span>
                </div>
            )}
        </div>
    );
}
