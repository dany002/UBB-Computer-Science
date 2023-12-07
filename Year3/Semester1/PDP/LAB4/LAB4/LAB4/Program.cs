// See https://aka.ms/new-console-template for more information
List<string> urls =  new() {
    "www.wonderfullushbrightspell.neverssl.com/",
    "targetedattacks.trendmicro.com/",
    "streamhd4k.com/",
    "pageometry.weebly.com/"
};

while (true)
{
    Console.WriteLine("1. Callback Solution");
    Console.WriteLine("2. Futures Solution");
    Console.WriteLine("3. Async Await Solution");
    string choice = Console.ReadLine();
    switch (choice)
    {
        case "1":
            new LAB4.CallbackSolution().Run(urls);
            break;
        case "2":
            new LAB4.FuturesSolution().Run(urls);
            break;
        case "3":
            new LAB4.AsyncAwaitSolution().Run(urls);
            break;
        default:
            Console.WriteLine("Invalid choice");
            return;
    }
    
}
