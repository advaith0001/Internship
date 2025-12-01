import Groq from "groq-sdk";

export async function POST(req) {
  try {
    const { text } = await req.json();

    if (!text) {
      return Response.json({ error: "No text provided" }, { status: 400 });
    }

    const groq = new Groq({
      apiKey: process.env.GROQ_API_KEY,
    });

    const completion = await groq.chat.completions.create({
      model: "llama-3.1-8b-instant",  
      messages: [
        {
          role: "system",
          content: "Summarize the text clearly in simple language.",
        },
        {
          role: "user",
          content: text,
        },
      ],
    });

    const summary = completion.choices[0].message.content;
    return Response.json({ summary });

  } catch (error) {
    console.error("GROQ ERROR:", error);
    return Response.json({ error: error.message }, { status: 500 });
  }
}
