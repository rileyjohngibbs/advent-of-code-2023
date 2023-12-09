export default function UnsolvedStack({ historyStack, extended }: { historyStack: number[][], extended: boolean }) {
    return <div className="flex flex-col">{
        historyStack.map((history, i) => {
            return <div key={i} className="flex flex-row gap-2">{
                history.map((temp, j) => {
                    const className = extended ? j % (history.length - 1) ? historyStack.length > 1 ? "" : "opacity-50" : "font-bold" : ""
                    return <div className={className} key={j}>{temp}</div>
        })
            }</div>
        })
    }</div>
}