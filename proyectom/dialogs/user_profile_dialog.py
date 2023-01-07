# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.dialogs import (
    ComponentDialog,
    WaterfallDialog,
    WaterfallStepContext,
    DialogTurnResult,
)
from botbuilder.dialogs.prompts import (
    TextPrompt,
    ChoicePrompt,
    ConfirmPrompt,
    PromptOptions,
)
from botbuilder.dialogs.choices import Choice
from botbuilder.core import MessageFactory, UserState

from data_models import UserProfile
from Algoritmo_Preguntas import *
Pregunta=sumapreguntas()


class UserProfileDialog(ComponentDialog):
    def __init__(self, user_state: UserState):
        super(UserProfileDialog, self).__init__(UserProfileDialog.__name__)

        self.user_profile_accessor = user_state.create_property("UserProfile")

        self.add_dialog(
            WaterfallDialog(
                WaterfallDialog.__name__,
                [
                    self.pregunta1_step,
                    self.pregunta2_step,
                    self.pregunta3_step,
                    self.pregunta4_step,
                    self.pregunta5_step,
                    self.pregunta6_step,
                    self.pregunta7_step,
                    self.pregunta8_step,
                    self.pregunta9_step,
                    self.email_step,
                    self.name_step,
                    self.confirm_step,
                    self.summary_step,
                ],
            )
        )
        self.add_dialog(TextPrompt(TextPrompt.__name__))
        self.add_dialog(ChoicePrompt(ChoicePrompt.__name__))
        self.add_dialog(ConfirmPrompt(ConfirmPrompt.__name__))
        self.initial_dialog_id = WaterfallDialog.__name__

    async def pregunta1_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        # WaterfallStep always finishes with the end of the Waterfall or with another dialog;
        # here it is a Prompt Dialog. Running a prompt here means the next WaterfallStep will
        # be run when the users response is received.
        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Teclea del 1 al 4 para contestar las siguientes 9 preguntas. \n Durante las últimas 2 semanas, ¿con qué frecuencia ha sentido molestias por los siguientes problemas."+"\n" + "Pregunta 1. Tener poco interés o placer en hacer las cosas"),
                choices=[Choice("NUNCA"), Choice("VARIOS DÍAS"), Choice("MÁS DE LA MITAD DE LOS DÍAS"), Choice("CASI TODOS LOS DÍAS")],
            ),
        )

    
    async def pregunta2_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        step_context.values["pregunta1"] = step_context.result.value
        # WaterfallStep always finishes with the end of the Waterfall or with another dialog;
        # here it is a Prompt Dialog. Running a prompt here means the next WaterfallStep will
        # be run when the users response is received.
        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Pregunta 2. Sentirse desanimado/a, deprimido/a, o sin esperanza"),
                choices=[Choice("NUNCA"), Choice("VARIOS DÍAS"), Choice("MÁS DE LA MITAD DE LOS DÍAS"), Choice("CASI TODOS LOS DÍAS")],
            ),
        )

    async def pregunta3_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        step_context.values["pregunta2"] = step_context.result.value
        # WaterfallStep always finishes with the end of the Waterfall or with another dialog;
        # here it is a Prompt Dialog. Running a prompt here means the next WaterfallStep will
        # be run when the users response is received.
        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Pregunta 3. Con problemas en dormirse o en mantenerse dormido/a, o en dormir demasiado"),
                choices=[Choice("NUNCA"), Choice("VARIOS DÍAS"), Choice("MÁS DE LA MITAD DE LOS DÍAS"), Choice("CASI TODOS LOS DÍAS")],
            ),
        )
    
    async def pregunta4_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        step_context.values["pregunta3"] = step_context.result.value
        # WaterfallStep always finishes with the end of the Waterfall or with another dialog;
        # here it is a Prompt Dialog. Running a prompt here means the next WaterfallStep will
        # be run when the users response is received.
        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Pregunta 4. Sentirse cansado/a o tener poca energía"),
                choices=[Choice("NUNCA"), Choice("VARIOS DÍAS"), Choice("MÁS DE LA MITAD DE LOS DÍAS"), Choice("CASI TODOS LOS DÍAS")],
            ),
        )

    async def pregunta5_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        step_context.values["pregunta4"] = step_context.result.value
        # WaterfallStep always finishes with the end of the Waterfall or with another dialog;
        # here it is a Prompt Dialog. Running a prompt here means the next WaterfallStep will
        # be run when the users response is received.
        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Pregunta 5. Tener poco apetito o comer en exceso"),
                choices=[Choice("NUNCA"), Choice("VARIOS DÍAS"), Choice("MÁS DE LA MITAD DE LOS DÍAS"), Choice("CASI TODOS LOS DÍAS")],
            ),
        )

    async def pregunta6_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        step_context.values["pregunta5"] = step_context.result.value
        # WaterfallStep always finishes with the end of the Waterfall or with another dialog;
        # here it is a Prompt Dialog. Running a prompt here means the next WaterfallStep will
        # be run when the users response is received.
        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Pregunta 6. Sentir falta de amor propio - o que sea un fracaso o que decepcionara a si mismo/a su familia"),
                choices=[Choice("NUNCA"), Choice("VARIOS DÍAS"), Choice("MÁS DE LA MITAD DE LOS DÍAS"), Choice("CASI TODOS LOS DÍAS")],
            ),
        )

    async def pregunta7_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        step_context.values["pregunta6"] = step_context.result.value
        # WaterfallStep always finishes with the end of the Waterfall or with another dialog;
        # here it is a Prompt Dialog. Running a prompt here means the next WaterfallStep will
        # be run when the users response is received.
        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Pregunta 7. Tener dificultad para concentrarse en cosas tales como leer el periódico o mirar la televisión"),
                choices=[Choice("NUNCA"), Choice("VARIOS DÍAS"), Choice("MÁS DE LA MITAD DE LOS DÍAS"), Choice("CASI TODOS LOS DÍAS")],
            ),
        )

    async def pregunta8_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        step_context.values["pregunta7"] = step_context.result.value
        # WaterfallStep always finishes with the end of the Waterfall or with another dialog;
        # here it is a Prompt Dialog. Running a prompt here means the next WaterfallStep will
        # be run when the users response is received.
        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Pregunta 8. Se mueve o habla tan lentamente que otra gente se podría dar cuenta"),
                choices=[Choice("NUNCA"), Choice("VARIOS DÍAS"), Choice("MÁS DE LA MITAD DE LOS DÍAS"), Choice("CASI TODOS LOS DÍAS")],
            ),
        )

    async def pregunta9_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        step_context.values["pregunta8"] = step_context.result.value
        # WaterfallStep always finishes with the end of the Waterfall or with another dialog;
        # here it is a Prompt Dialog. Running a prompt here means the next WaterfallStep will
        # be run when the users response is received.
        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Pregunta 9. Se la han ocurrido pensamientos de que sería mejor estar muerto/a o de que haría daño de alguna manera"),
                choices=[Choice("NUNCA"), Choice("VARIOS DÍAS"), Choice("MÁS DE LA MITAD DE LOS DÍAS"), Choice("CASI TODOS LOS DÍAS")],
            ),
        )
    
    async def email_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        step_context.values["pregunta9"] = step_context.result.value
        # WaterfallStep always finishes with the end of the Waterfall or with another dialog;
        # here it is a Prompt Dialog. Running a prompt here means the next WaterfallStep will
        # be run when the users response is received.
        return await step_context.prompt(
            TextPrompt.__name__,
            PromptOptions(prompt=MessageFactory.text("Please enter your email.")),
        )


    async def name_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        step_context.values["email"] = step_context.result

        return await step_context.prompt(
            TextPrompt.__name__,
            PromptOptions(prompt=MessageFactory.text("Please enter your name.")),
        )

   
    async def confirm_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        step_context.values["name"] = step_context.result
        


        # WaterfallStep always finishes with the end of the Waterfall or
        # with another dialog; here it is a Prompt Dialog.
        return await step_context.prompt(
            ConfirmPrompt.__name__,
            PromptOptions(prompt=MessageFactory.text("Is this ok?")),
        )

    async def summary_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        if step_context.result:
            # Get the current profile object from user state.  Changes to it
            # will saved during Bot.on_turn.
            user_profile = await self.user_profile_accessor.get(
                step_context.context, UserProfile
            )

            user_profile.pregunta1 = step_context.values["pregunta1"]
            user_profile.pregunta2 = step_context.values["pregunta2"]
            user_profile.pregunta3 = step_context.values["pregunta3"]
            user_profile.pregunta4 = step_context.values["pregunta4"]
            user_profile.pregunta5 = step_context.values["pregunta5"]
            user_profile.pregunta6 = step_context.values["pregunta6"]
            user_profile.pregunta7 = step_context.values["pregunta7"]
            user_profile.pregunta8 = step_context.values["pregunta8"]
            user_profile.pregunta9 = step_context.values["pregunta9"]
            user_profile.name = step_context.values["name"]
            user_profile.email = step_context.values["email"]
            Pregunta.respuesta(step_context.values["pregunta1"])
            Pregunta.respuesta(step_context.values["pregunta2"])
            Pregunta.respuesta(step_context.values["pregunta3"])
            Pregunta.respuesta(step_context.values["pregunta4"])
            Pregunta.respuesta(step_context.values["pregunta5"])
            Pregunta.respuesta(step_context.values["pregunta6"])
            Pregunta.respuesta(step_context.values["pregunta7"])
            Pregunta.respuesta(step_context.values["pregunta8"])
            Pregunta.respuesta(step_context.values["pregunta9"])
            score_total=Pregunta.diagnostico()
            Pregunta.preguntasaBD()
            Pregunta.datos_usuario(step_context.values["name"],step_context.values["email"])
            
           

            msg = f"La respuesta de la pregunta 1 fue {user_profile.pregunta1}, pregunta 2: {user_profile.pregunta2}, pregunta 3: {user_profile.pregunta3}, pregunta 4: {user_profile.pregunta4}, pregunta 5: {user_profile.pregunta5}, pregunta 6: {user_profile.pregunta6}, pregunta 7: {user_profile.pregunta7}, pregunta 8: {user_profile.pregunta8}, pregunta 9: {user_profile.pregunta9}  y tu nombre es {user_profile.name} , tu correo es {user_profile.email} y tu score total es {score_total}."
        

            await step_context.context.send_activity(MessageFactory.text(msg))

            
        else:
            await step_context.context.send_activity(
                MessageFactory.text("Thanks. Your profile will not be kept.")
            )

        # WaterfallStep always finishes with the end of the Waterfall or with another
        # dialog, here it is the end.
        return await step_context.end_dialog()

    