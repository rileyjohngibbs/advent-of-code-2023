import { readFileSync } from "node:fs";
import SolutionStepper from "./SolutionStepper";

export default function Day02() {

    const inputLines = readFileSync("../inputs/09.txt", "utf-8").split("\n").filter(x => x)
    
    return <main className="flex flex-col">
        <SolutionStepper inputLines={inputLines} />
    </main>
}